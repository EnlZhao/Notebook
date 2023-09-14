# Tensors ｜ 张量

- Tensors 是类似 arrays 和 matrices 的数据结构 (在 Pytorch 中使用 tensors 来编码模型的输入和输出，以及模型的参数)
- Tensors 类似于 Numpy 的 ndarrays，但是可以在 GPU 或其他特殊硬件上使用来加速计算

``` python
import torch
import numpy as np
```

## Tensor Initialization

- Tensor 可以通过多种方式进行初始化

### Directly from data

- Tensor 可以直接从 data 中进行初始化 (数据类型会自动推断)

``` python
data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
```

### From a NumPy array

- Tensor 可以从 NumPy array 中进行初始化，并且保留 NumPy array 的维度和数据类型 (反之亦然, see [Bridge with NumPy](#bridge-with-numpy)

``` python
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
```

### From another tensor

- 新的 tensor 保留了原始 tensor 的属性 (shape, datatype)，除非被显式地重写

=== "code"
    ``` python
    x_ones = torch.ones_like(x_data) # retains the properties of x_data
    print(f"Ones Tensor: \n {x_ones} \n")

    x_rand = torch.rand_like(x_data, dtype=torch.float) # overrides the datatype of x_data
    print(f"Random Tensor: \n {x_rand} \n")
    ```

=== "output"
    ``` output
    Ones Tensor: 
     tensor([[1, 1],
            [1, 1]])

    Random Tensor:
     tensor([[0.7576, 0.2793],
            [0.4031, 0.7347]])
    ```

### With random or constant values

- `shape` 是 tensor 维度的元组(tuple), 上面的函数中，它确定了输出张量的维度

=== "code"
    ``` python
    shape = (2, 3,) # tuple of tensor dimensions
    rand_tensor = torch.rand(shape)
    ones_tensor = torch.ones(shape)
    zeros_tensor = torch.zeros(shape)

    print(f"Random Tensor: \n {rand_tensor} \n")
    print(f"Ones Tensor: \n {ones_tensor} \n")
    print(f"Zeros Tensor: \n {zeros_tensor}")
    ```
=== "output"
    ``` output
    Random Tensor:
    tensor([[0.3904, 0.6009, 0.2566],
            [0.7936, 0.9408, 0.1332]])

    Ones Tensor:
    tensor([[1., 1., 1.],
            [1., 1., 1.]])

    Zeros Tensor:
    tensor([[0., 0., 0.],
            [0., 0., 0.]])

## Tensor Attributes

- Tensor attributrs describe their shape, datatype, and the device on which they are stored

=== "code"
    ``` python
    tensor = torch.rand(3, 4)

    print(f"Shape of tensor: {tensor.shape}")
    print(f"Datatype of tensor: {tensor.dtype}")
    print(f"Device tensor is stored on: {tensor.device}")
    ```
=== "output"
    ``` output
    Shape of tensor: torch.Size([3, 4])
    Datatype of tensor: torch.float32
    Device tensor is stored on: cpu
    ```

## Tensor Operations

- Over 100 tensor operations, including transposing, indexing, slicing, mathematical operations, linear algebra, random sampling, and more are comprehensively described [here](https://pytorch.org/docs/stable/torch.html).
- 这些操作都能在 GPU 上运行（通常比在 CPU 上运行速度更快）

=== "code"
    ```python
    # We move our tensor to the GPU if available
    if torch.cuda.is_available():
        tensor = tensor.to('cuda')
        print(f"Device tensor is stored on: {tensor.device}")
    ```
=== "output"
    ``` output
    Device tensor is stored on: cuda:0
    ```

### Some operations

> If you’re familiar with the NumPy API, you’ll find the Tensor API a breeze to use.

#### Standard numpy-like indexing and slicing

=== "code"
    ``` python
    tensor = torch.ones(4, 4)
    tensor[:,1] = 0
    print(tensor)
    ```
=== "output"
    ``` output
    tensor([[1., 0., 1., 1.],
            [1., 0., 1., 1.],
            [1., 0., 1., 1.],
            [1., 0., 1., 1.]])
    ```

#### Joining tensors

- We can use `torch.cat` to concatenate a sequence of tensors along a given dimension. 

> - See also [torch.stack](https://pytorch.org/docs/stable/generated/torch.stack.html#torch.stack) and [torch.split](https://pytorch.org/docs/stable/generated/torch.split.html#torch.split)
> - another tensor joining op that is subtly different from `torch.cat`.

=== "code"
    ``` python
    t1 = torch.cat([tensor, tensor, tensor], dim=1)
    print(t1)
    ```
=== "output"
    ``` output
    tensor([[1., 0., 1., 1., 1., 0., 1., 1., 1., 0., 1., 1.],
            [1., 0., 1., 1., 1., 0., 1., 1., 1., 0., 1., 1.],
            [1., 0., 1., 1., 1., 0., 1., 1., 1., 0., 1., 1.],
            [1., 0., 1., 1., 1., 0., 1., 1., 1., 0., 1., 1.]])

#### Multiplying tensors

- Computing the element-wise product

    === "code"
        ``` python
        # This computes the element-wise product
        print(f"tensor.mul(tensor) \n {tensor.mul(tensor)} \n")
        # Alternative syntax:
        print(f"tensor * tensor \n {tensor * tensor}")
        ```
    === "output"
        ``` output
        tensor.mul(tensor)
        tensor([[1., 0., 1., 1.],
                [1., 0., 1., 1.],
                [1., 0., 1., 1.],
                [1., 0., 1., 1.]])

        tensor * tensor
        tensor([[1., 0., 1., 1.],
                [1., 0., 1., 1.],
                [1., 0., 1., 1.],
                [1., 0., 1., 1.]])
        ```

- Computing the matrix multiplication between two tensors

    === "code"
        ``` python
        print(f"tensor.matmul(tensor.T) \n {tensor.matmul(tensor.T)} \n")
        # Alternative syntax:
        print(f"tensor @ tensor.T \n {tensor @ tensor.T}")
        ```
    === "output"
        ``` output
        tensor.matmul(tensor.T)
        tensor([[3., 3., 3., 3.],
                [3., 3., 3., 3.],
                [3., 3., 3., 3.],
                [3., 3., 3., 3.]])

        tensor @ tensor.T
        tensor([[3., 3., 3., 3.],
                [3., 3., 3., 3.],
                [3., 3., 3., 3.],
                [3., 3., 3., 3.]])
        ```

#### In-place operations

- Operations that have a `_` suffix are in-place
- 这种操作会改变被操作的张量本身，例如 `x.copy_(y)`, `x.t_()`, 将会改变 `x`

??? note 
    In-place operations 可以节省一些内存，但在计算导数时会丢失历史信息。因此，不鼓励使用它们。

=== "code"
    ``` python
    # tensor.add_(5)
    tensor.add_(5)
    print(tensor)
    ```
=== "output"
    ``` output
    tensor([[6., 5., 6., 6.],
            [6., 5., 6., 6.],
            [6., 5., 6., 6.],
            [6., 5., 6., 6.]])
    ```

## Bridge with NumPy

> Tensors on the CPU and NumPy arrays can share their underlying memory locations, and changing one will change the other.

### Tensor to NumPy array

=== "code"
    ``` python
    t = torch.ones(5)
    print(f"t: {t}")
    n = t.numpy()
    print(f"n: {n}")
    ```
=== "output"
    ``` output
    t: tensor([1., 1., 1., 1., 1.])
    n: [1. 1. 1. 1. 1.]
    ```

- A change in the tensor reflects in the NumPy array.

=== "code"
    ``` python
    t.add_(1)
    print(f"t: {t}")
    print(f"n: {n}")
    ```
=== "output"
    ``` output
    t: tensor([2., 2., 2., 2., 2.])
    n: [2. 2. 2. 2. 2.]
    ```

### NumPy array to Tensor

``` python
np = np.ones(5)
t = torch.from_numpy(np)
```

- Changes in the NumPy array reflects in the tensor.

=== "code"
    ``` python
    np.add(n, 1, out=n)
    print(f"t: {t}")
    print(f"np: {np}")
    ```
=== "output"
    ``` output
    t: tensor([2., 2., 2., 2., 2.], dtype=torch.float64)
    n: [2. 2. 2. 2. 2.]





