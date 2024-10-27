# 绪论

!!! def
    - 机器学习所研究的主要内容是关于在计算机上从数据中产生“模型” (model) 的算法，即“学习算法” (learning algorithm)。
    - 有了学习算法，计算机可以根据我们提供的数据生成“模型”，并用这个模型来预测新数据的性质。
    - 也可以说，机器学习是研究关于“学习算法”的学问。

> 本书中的“模型”泛指从数据中学得的结果

## 基本术语

假设我们收集了一批西瓜的数据，例如：(色泽=青绿;根蒂=蜷缩;敲声=浊响)， (色泽=乌黑;根蒂=稍蜷;敲声=沉闷)， (色泽=浅自;根蒂=硬挺;敲声=清脆)……每对括号内是一个西瓜的记录，“=”意思是“取值为”。

- 所有记录的集合为：数据集 (data set)。
- 每一条记录是关于一个事件或对象（这里是一个西瓜）的描述，称为：一个示例（instance）或样本（sample）。
- 例如：色泽或敲声，单个的特点为特征（feature）或属性（attribute）。
    - 而属性上的取值，例如：青绿、乌黑、浅自等，为属性值（attribute value）。
    - 属性张成的空间为：属性空间（feature space）、输入空间（input space）或样本空间（sample space）。
- 对于一条记录，如果在坐标轴上表示，每个西瓜都可以用坐标轴中的一个点表示，一个点也是一个向量，例如（青绿，蜷缩，浊响），即每个西瓜为：一个特征向量（feature vector）。
- 一个样本的特征数为：维数（dimensionality），该西瓜的例子维数为3，当维数非常大时，也就是现在说的“维数灾难”。

- 一般，令 $D=\{\boldsymbol{x}_1,\boldsymbol{x}_2,\ldots,\boldsymbol{x}_m\}$ 表示包含 m 个示例的数据集
    - 其中 $\boldsymbol{x}_i=(x_{i1};x_{i2};\ldots;x_{id})$ 表示第 $i$ 个示例，$d$ 表示示例 $\boldsymbol{x}_i$ 的维数，$m$ 表示示例的总数。
- 学得模型对应了关于数据的某种潜在的规律，因此也称为 **假设（hypothesis）。**
    - 这种潜在规律自身，被称为 **“真相”或“真实”（ground-truth）。**

---

- 可以想象，如果希望学习到一个帮助判断未知西瓜好坏的模型，仅有前面的示例数据是不够的。
- 要建立这样的关于“预测”的模型，还需要训练样本的“结果”信息，即：**标记（label）或响应（response）。**
    - 例如 “((色泽=青绿;根蒂=蜷缩;敲声=浊响)，好瓜)”。
    - 这里，“好瓜”就称为示例的标记。拥有标记的示例称为 **“样例”（example）。**
    - 一般使用，$(\boldsymbol{x}_i, y_i)$ 表示第 $i$ 个样例，其中 $y_i \in \mathcal{Y}$ 是示例 $\boldsymbol{x}_i$ 的标记，$\mathcal{Y}$ 是所有标记的集合，称为 **标记空间（label space）**。

!!! def "预测任务"
    - “分类” (classification) 任务：预测的是离散值，如好瓜/坏瓜。
    - “回归” (regression) 任务：预测的是连续值，如西瓜成熟度。
    - 一般预测任务是希望通过对训练集进行学习，建立一个从输入空间 $\mathcal{X}$ 到输出空间 $\mathcal{Y}$ 的映射，即：$f: \mathcal{X} \to \mathcal{Y}$。
        - 对于二分类 (binary classification) 任务，通常令 $\mathcal{Y}=\{+1, -1\}$ 或 $\{0, 1\}$。
        - 对于多分类 (multi-class classification) 任务，$| \mathcal{Y} | > 2$.
        - 对于回归任务，$\mathcal{Y}=\mathbb{R}$，即实数集。

学得模型后，使用其进行预测的过程，称为 **测试（testing）** 或 **预测（prediction）**。

- 被预测的样本，称为 **测试样本（test sample）**。例如在学得 $f$ 后，对于新的样本 $\boldsymbol{x}$，得到其预测标记 $y = f(\boldsymbol{x})$。


