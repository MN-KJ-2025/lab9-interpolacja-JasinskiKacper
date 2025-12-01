# =================================  TESTY  ===================================
# Testy do tego pliku obejmują jedynie weryfikację poprawności wyników dla
# prawidłowych danych wejściowych - obsługa niepoprawych danych wejściowych
# nie jest ani wymagana ani sprawdzana. W razie potrzeby lub chęci można ją 
# wykonać w dowolny sposób we własnym zakresie.
# =============================================================================
import numpy as np


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
    
    if n == 1:
        return np.array([1.0])
    
    res = np.zeros(n)
    for k in range(n):
        res[k] = np.cos((np.pi * k) / (n - 1))
    
    return np.sort(res)[::-1]
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
    
    w = np.zeros(n)
    for i in range(n):
        if i == 0 or i == (n - 1):
            w[i] = 0.5 * ((-1) ** i )
        else:
            w[i] = (-1) ** i
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
    
    Y = np.zeros(x.size)
    for j in range(x.size):
        idx = np.where(x[j] == xi)[0]
        if idx.size > 0:
            Y[j] = yi[idx[0]]
            continue
        else:
            L = wi / (x[j] - xi)
            Y[j] = np.sum(L * yi) / np.sum(L)
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
    
    if isinstance(xr, (int, float)) and isinstance(x, (int, float)):
        return abs(xr - x)
    
    xr = np.array(xr, dtype=float)
    x = np.array(x, dtype=float)

    if xr.shape != x.shape:
        return None
    
    diff = np.abs(xr - x)
    return float(np.max(diff))
    pass
