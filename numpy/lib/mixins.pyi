from typing import List
from abc import ABCMeta, abstractmethod

__all__: List[str]

# NOTE: `NDArrayOperatorsMixin` is not formally an abstract baseclass,
# even though it's relient on subclasses implementing `__array_ufunc__`

class NDArrayOperatorsMixin(metaclass=ABCMeta):
    @abstractmethod
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __iadd__(self, other): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __isub__(self, other): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __imul__(self, other): ...
    def __matmul__(self, other): ...
    def __rmatmul__(self, other): ...
    def __imatmul__(self, other): ...
    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...
    def __itruediv__(self, other): ...
    def __floordiv__(self, other): ...
    def __rfloordiv__(self, other): ...
    def __ifloordiv__(self, other): ...
    def __mod__(self, other): ...
    def __rmod__(self, other): ...
    def __imod__(self, other): ...
    def __divmod__(self, other): ...
    def __rdivmod__(self, other): ...
    def __pow__(self, other): ...
    def __rpow__(self, other): ...
    def __ipow__(self, other): ...
    def __lshift__(self, other): ...
    def __rlshift__(self, other): ...
    def __ilshift__(self, other): ...
    def __rshift__(self, other): ...
    def __rrshift__(self, other): ...
    def __irshift__(self, other): ...
    def __and__(self, other): ...
    def __rand__(self, other): ...
    def __iand__(self, other): ...
    def __xor__(self, other): ...
    def __rxor__(self, other): ...
    def __ixor__(self, other): ...
    def __or__(self, other): ...
    def __ror__(self, other): ...
    def __ior__(self, other): ...
    def __neg__(self): ...
    def __pos__(self): ...
    def __abs__(self): ...
    def __invert__(self): ...
