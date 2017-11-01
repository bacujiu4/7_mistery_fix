# Решатель квадратных уравнений

Программа вычисляет действительные корни квадратного уравнения.

# Как использовать

Функция get_roots принимает на вход 3 аргумента: старший коэффициент, средний коэффициент и свободный член. Aункция возвращает значения корней.
Если конрня или корней нет, то возвращает None:

```python
from quadratic_equation import get_roots
get_roots(1, -2, 1)
(1.0, None)
get_roots(1, 2, -3)
(-3.0,1.0)
```

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
