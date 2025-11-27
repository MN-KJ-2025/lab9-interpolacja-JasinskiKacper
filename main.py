# =================================  TESTY  ===================================
# Testy do tego pliku obejmują jedynie weryfikację poprawności wyników dla
# prawidłowych danych wejściowych - obsługa niepoprawych danych wejściowych
# nie jest ani wymagana ani sprawdzana. W razie potrzeby lub chęci można ją 
# wykonać w dowolny sposób we własnym zakresie.
# =============================================================================
import numpy as np

f1 = lambda x: np.sign(x) * x + x ** 2
f2 = lambda x: np.sign(x) * (x ** 2)
f3 = lambda x: (abs(np.sin(5 * x))) ** 3
f4_1 = lambda x: 1 / (1 + 1 * (x ** 2))
f4_25 = lambda x: 1 / (1 + 25 * (x ** 2))
f4_100 = lambda x: 1 / (1 + 100 * (x ** 2))
f5 = lambda x: np.sign(x)

def chebyshev_nodes(n: int = 10) -> np.ndarray | None:
    """Funkcja generująca wektor węzłów Czebyszewa drugiego rodzaju (n,) 
    i sortująca wynik od najmniejszego do największego węzła.

    Args:
        n (int): Liczba węzłów Czebyszewa.
    
    Returns:
        (np.ndarray): Wektor węzłów Czebyszewa (n,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    if not isinstance(n, int) or n <= 0:
        return None
    
    res = np.ndarray([])
    for k in range(0, n + 1):
        x_k = np.cos((np.pi * np.arange(n)) / (n - 1))
        np.append(res, x_k)
    return res
    pass


def bar_cheb_weights(n: int = 10) -> np.ndarray | None:
    """Funkcja tworząca wektor wag dla węzłów Czebyszewa wymiaru (n,).

    Args:
        n (int): Liczba wag węzłów Czebyszewa.
    
    Returns:
        (np.ndarray): Wektor wag dla węzłów Czebyszewa (n,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    if not isinstance(n, int) or n <= 0:
        return None
    w = np.ndarray([])
    for i in range(0, n + 1):
        if i == 0 or i == n:
            np.append(w, (-1) ** i * 0.5)
        else:
            np.append(w, (-1) ** i * 1)
    return w
    pass


def barycentric_inte(
    xi: np.ndarray, yi: np.ndarray, wi: np.ndarray, x: np.ndarray
) -> np.ndarray | None:
    """Funkcja przeprowadza interpolację metodą barycentryczną dla zadanych 
    węzłów xi i wartości funkcji interpolowanej yi używając wag wi. Zwraca 
    wyliczone wartości funkcji interpolującej dla argumentów x w postaci 
    wektora (n,).

    Args:
        xi (np.ndarray): Wektor węzłów interpolacji (m,).
        yi (np.ndarray): Wektor wartości funkcji interpolowanej w węzłach (m,).
        wi (np.ndarray): Wektor wag interpolacji (m,).
        x (np.ndarray): Wektor argumentów dla funkcji interpolującej (n,).
    
    Returns:
        (np.ndarray): Wektor wartości funkcji interpolującej (n,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    if not isinstance(xi, np.ndarray) or not isinstance(yi, np.ndarray):
        return None
    if not isinstance(wi, np.ndarray) or not isinstance(x, np.ndarray):
        return None
    if xi.size != yi.size or xi.size != wi.size:
        return None
    
    Y = np.ndarray([])
    for j in range(x.size):
        L = wi[j] / (x[j] - xi[j])
        np.append(Y, yi[j] @ L / np.sum(L))
    return Y
    pass


def L_inf(
    xr: int | float | list | np.ndarray, x: int | float | list | np.ndarray
) -> float | None:
    """Funkcja obliczająca normę L-nieskończoność. Powinna działać zarówno na 
    wartościach skalarnych, listach, jak i wektorach biblioteki numpy.

    Args:
        xr (int | float | list | np.ndarray): Wartość dokładna w postaci 
            skalara, listy lub wektora (n,).
        x (int | float | list | np.ndarray): Wartość przybliżona w postaci 
            skalara, listy lub wektora (n,).

    Returns:
        (float): Wartość normy L-nieskończoność.
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    if not isinstance(xr, (int, float, list, np.ndarray)):
        return None
    if not isinstance(x, (int, float, list, np.ndarray)):
        return None
    if xr.size != x.size:
        return None
    
    if isinstance(xr, (int, float)) and isinstance(x, (int, float)):
        return abs(xr - x)
    elif isinstance(xr, list) and isinstance(x, list):
        diff = []
        for i in range(len(xr)):
            diff = abs(xr[i] - x[i])
        return max(diff)
    pass
