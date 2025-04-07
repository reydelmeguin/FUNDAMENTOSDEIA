import numpy as np
from collections import Counter
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# ================== 🌳 1. Clase para un Árbol de Decisión ==================
class DecisionTree:
    def __init__(self, max_depth=3):
        self.max_depth = max_depth
    
    def fit(self, X, y):
        self.tree = self._build_tree(X, y, depth=0)
    
    def _build_tree(self, X, y, depth):
        # Si alcanzamos la profundidad máxima o todas las clases son iguales, devolvemos una hoja
        if depth == self.max_depth or len(set(y)) == 1:
            return {'class': Counter(y).most_common(1)[0][0]}
        
        # Encuentra la mejor división (característica y umbral)
        best_feature, best_threshold = self._find_best_split(X, y)
        
        # Divide los datos
        left_mask = X[:, best_feature] <= best_threshold
        right_mask = ~left_mask
        
        # Construye los subárboles izquierdo y derecho
        left_tree = self._build_tree(X[left_mask], y[left_mask], depth + 1)
        right_tree = self._build_tree(X[right_mask], y[right_mask], depth + 1)
        
        return {
            'feature': best_feature,
            'threshold': best_threshold,
            'left': left_tree,
            'right': right_tree
        }
    
    def _find_best_split(self, X, y):
        best_gini = float('inf')
        best_feature, best_threshold = None, None
        
        for feature in range(X.shape[1]):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                left_mask = X[:, feature] <= threshold
                gini = self._gini_impurity(y[left_mask], y[~left_mask])
                if gini < best_gini:
                    best_gini = gini
                    best_feature = feature
                    best_threshold = threshold
        return best_feature, best_threshold
    
    def _gini_impurity(self, left_y, right_y):
        n_left, n_right = len(left_y), len(right_y)
        total = n_left + n_right
        
        # Calcula la impureza de Gini para cada lado
        p_left = np.sum([(np.sum(left_y == c) / n_left) ** 2 for c in set(left_y)])
        p_right = np.sum([(np.sum(right_y == c) / n_right) ** 2 for c in set(right_y)])
        
        gini_left = 1 - p_left
        gini_right = 1 - p_right
        
        # Promedio ponderado
        return (n_left / total) * gini_left + (n_right / total) * gini_right
    
    def predict(self, X):
        return np.array([self._predict_tree(x, self.tree) for x in X])
    
    def _predict_tree(self, x, node):
        if 'class' in node:
            return node['class']
        if x[node['feature']] <= node['threshold']:
            return self._predict_tree(x, node['left'])
        else:
            return self._predict_tree(x, node['right'])

# ================== 🌲🌲 2. Clase para el Random Forest ==================
class RandomForest:
    def __init__(self, n_trees=10, max_depth=3):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.trees = []
    
    def fit(self, X, y):
        self.trees = []
        for _ in range(self.n_trees):
            # Muestreo bootstrap (con reemplazo)
            sample_idx = np.random.choice(len(X), len(X), replace=True)
            X_sample, y_sample = X[sample_idx], y[sample_idx]
            
            # Entrena un árbol con una selección aleatoria de características
            tree = DecisionTree(max_depth=self.max_depth)
            tree.fit(X_sample, y_sample)
            self.trees.append(tree)
    
    def predict(self, X):
        # Cada árbol vota y se elige la clase más frecuente
        tree_preds = np.array([tree.predict(X) for tree in self.trees])
        return np.array([Counter(tree_preds[:, i]).most_common(1)[0][0] for i in range(len(X))])

# ================== 🔍 3. Probamos el modelo ==================
# Generamos datos de ejemplo (2 clases, 5 características)
X, y = make_classification(n_samples=100, n_features=5, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenamos el Random Forest con 5 árboles
rf = RandomForest(n_trees=5, max_depth=2)
rf.fit(X_train, y_train)

# Predecimos en los datos de prueba
predictions = rf.predict(X_test)

# Calculamos la precisión
accuracy = np.mean(predictions == y_test)
print(f"🔹 Precisión del Random Forest: {accuracy * 100:.2f}%")