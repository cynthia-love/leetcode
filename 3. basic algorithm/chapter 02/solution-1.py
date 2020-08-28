# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    第2章, 面向对象编程
"""
"""
    设计目标、设计原则、设计模式
    其中设计模式包括: 算法设计模式(算法分析, 算法结构, 算法思想)+软件工程设计模式(创建型, 结构型, 行为型)
"""

"""
    基本概念
    
    1. 类class的实例instance称为对象object
    2. 类定义了对象的实例变量instance variable, 又称数据成员data member
       还定义了对象的可执行方法methods, 又称成员函数member function
    3. 面向对象的设计目标
       健壮性robustness, 不光可以处理正确输入, 还可以处理各种异常情况(同一环境统一应用下)
       适应性adaptability, 可以适应各种外部环境的变化, 比如硬件, 平台, 时间发展(跨环境)
       重用性reusability, 同样的代码可以用在不用的应用中(同一环境下跨应用)
    4. 面向对象的设计原则(模块化-健壮性, 重用性; 抽象化; 封装-健壮性, 适应性)
       模块化: 比如一所房子的电力系统, 热力系统, 水力系统等不同的功能单元, 比如python中的模块, 就是
              一个关系比较密切的函数和类的集合, 比如math, os. 模块化可以提升健壮性, 因为不同的组件易于
              测试和调试, 且问题比较容易定位到相对独立的特定组件; 模块化还可以提升重用性, 比如很多地方都
              能引入math, os等模块. 
       抽象化: 即从一个复杂的系统中提炼出最基础的部分, Abstract Data Types, ADT, 它定义了数据存储的
              类型和支持的操作, 其更关心要做什么而不是怎么做, 一般对应到interface而不是class
              Python里没有interface, 而是使用一种称为Abstract Base Class, ABC, 的机制, 其性质
              和interface差不多, 不能被实例化, 且继承类必须实现其规定的所有方法, 其应用场景包括
              希望判断某个对象的类型或强制继承类必须实现某些方法(python里的抽象基类主要在abc和
              collections.abc里). 注意, 虽然python里有抽象基类机制, 但不建议用, 因为python的
              风格更偏向于鸭子机制, 只要"一直鸟走起来像鸭子, 游起来像鸭子, 叫起来像鸭子, 就可以称为鸭子."
              比如def f(m): print(m[0]), 不会强制规定m的类型, 只要m支持数字索引, 那就能打印m[0]
              
       封装:  软件系统的不同组件不应该显示其各自实现的内部细节, 只需要保持一致的公共接口即可, 比如排序
             方法, 内部用哪种排序随便, 只要最终达到排序效果就行. 封装可以增加健壮性和适应性, 因为它
             允许修改程序的内部实现细节而不影响其他部分, 从而更容易修复漏洞(不会牵一发动全身)和给
             组件中增加对更多场景的适应性. 按照惯例, 在python里, 以_开头的数据成员和成员函数被认为
             是非公开的, 外部不应该直接用, 另外, 自动生成文档时也会自动忽略这些非公开成员.
"""
"""
    5. 设计模式!!!重要!!!
    设计模式, 即一种解决问题的模板, 告诉你在什么情况下应该用怎样的解决方案, 怎么用, 包括一个名称, 一个
    语境, 如何应用, 以及产出是什么. 分为两大类, 算法设计模式和软件工程模式
    
    (1) 算法设计模式
    算法分析相关的: 最好、最坏、平均、摊销(最坏情况下的平均)
    算法结构相关的: 非递归、递归
    算法思想相关的: 暴力 减治 分治 回溯 分支限界 贪心 动态规划, 这7个算法思想一定牢牢掌握 
    
    (2) 软件工程设计模式
    创建型模式: 工厂, 抽象工厂, 单例, 建造者, 原型
    结构型模式: 适配器, 装饰器, 代理, 外观, 桥接, 组合, 享元
    行为型模式: 策略, 模板, 观察者, 访问者, 中介者, 迭代器, 责任链, 命令, 备忘录, 状态, 解释器
    
    下面一个一个解释设计模式
    
"""

"""算法设计模式"""
# 1.1.1 算法设计模式-算法分析-最好
def find(l, target):
    for each in l:
        if each == target:
            return True
    return False
# 最理想情况下, 第一个就是要查找的数, 时间复杂度O(1)

# 1.1.2 算法设计模式-算法分析-最坏
# 同样分析上面那个函数, 最不理想情况下, 最后一个是/不是, 即n次, O(n)
# 注意, 最后一个是与不是, 都是查找n次都能确定的

# 1.1.3 算法设计模式-算法分析-平均
# 同样分析上面那个函数, 枚举所有情况, 复杂度求均值
# (1+2+3...+n+n)/(n+1) = n(n+3)/2/(n+1) = O(n)
# 注意这里假设每种情况是同概率的, 都是1/(n+1)
# 实际上概率不一样, 在里面和不在里面都是1/2, 所以前n种情况合起来概率才是1/2, 平均1/2n
# 所以加权平均时间复杂度为1/2n*1+1/2n*2+....+1/2n*n+1/2*n = (3n+1)/4 = O(n)

# 1.1.4 算法设计模式-算法分析-摊销(均摊)
# 本质上是一种特殊的加权平均, 适合那种周期性的, 大量低复杂度情况跟着个别高复杂度操作
def f(l, i):
    n = len(l)
    if i < n:
        l.insert(i, 10)
    else:
        print(sum(l))
        l.clear()
# 1 1 1 1 n...1 1 1 1 n, 当然, 可以去求加权平均, 也可以直接用均摊思想, 把耗时多的
# 复杂度分摊到耗时低的复杂度, n次插入O(1)跟着一次求和O(n), 很有规律性, 可以把O(n)摊销
# 到n次O(1)上去, 得到时间复杂度O(1)

# 1.2.1 算法设计模式-算法结构-非递归
# 大部分函数都是非递归

# 1.2.2 算法设计模式-算法结构-递归
# 递归, 即函数自己调自己, 可以把一个大型问题转化为一个与原问题类似的规模较小的问题
# 一般有着注入f(n) = a*f(n-1)+b这种结构, 当然有时候并不能直接写出来公式, 只是存在逻辑上的类似结构
# 比如汉诺塔, n个盘子由A移到C, 可以转化为n-1个盘子由A移到B, n号盘子由A移到C, n-1个盘子由B移到C
def f1(n):
    # n==1为边界条件
    if n == 1:
        return 1
    else:
        return n*f1(n-1)

# 1.3.1 算法设计模式-算法思想-暴力
# 遇到问题最最直接的思考方式, 比如在升序数组中查找数, 从头到尾遍历
# 再比如排列算法里的按数值进制暴力枚举所有可能情况, 再选出符合条件的
"""用状态空间树的思维去理解, 从根节点出发, 暴力法要走完所有的路径, 然后再判断所有解(可能是路径也可能直接是叶节点)是否符合要求"""
def f2(l, target):
    # l为升序
    for each in l:
        if each == target:
            return True
    return False

# 1.3.2 算法设计模式-算法思想-减治
# 减治将问题分解成子问题, 解就在其中一个子问题的解中, 范围不断缩小, 根节点到某一个叶节点, 其余子问题减去就好
# 分治将问题分解成子问题, 得到子问题的解之后还需要合并才能得到最终的解, 所有叶节点都要到达, 然后合并出根节点的解
# 一般情况下不特别区分减治, 而是将其划归到广义的分治中去
"""用状态空间树的思维去理解, 从根节点出发, 减治法能直接判断出下一步该走哪个子节点, 然后该子节点成为当前节点继续此过程"""
"""直到到达某个叶节点, 并可由该叶节点或(注意这里的或)路径上已经过的所有节点得出最终的解"""
def f3(l, target):
    # l升序
    def rf(left, right):
        if left > right:
            return False

        middle = (left+right)//2
        if l[middle] == target:
            return True
        # 注意下面两种情况, 实现了减治的效果, 只会走一个分支
        elif l[middle] > target:
            return rf(left, middle-1)
        else:
            return rf(middle+1, right)
    return rf(0, len(l)-1)

print(f3([1, 2, 3, 4], 5))
# 1.3.3 算法设计模式-算法思想-分治
# 减治将问题分解成子问题, 解就在其中一个子问题的解中, 其余子问题减去就好
# 分治将问题分解成子问题, 得到子问题的解之后还需要合并才能得到最终的解
# 一般情况下不特别区分减治, 而是将其划归到分治中去, 如果要严格区分分治的话
# 大概是下面这种形式
"""用状态空间树的思维去理解, 从根节点出发, 分治法需要到达所有叶节点, 其最终解由所有叶节点解合并得到"""
"""注意, 用分治法的解不能是根节点到叶节点的路径, 因为要求各子问题相互独立"""

def f4(l, target):
    # l什么顺序无所谓
    def rf(left, right):
        if left > right:
            return False
        middle = (left+right)//2
        if l[middle] == target:
            return True
        else:
            # 与减治相比, 这里没有减, 问题的解依赖所有子问题的解
            return rf(left, middle-1) or rf(middle+1, right)
    return rf(0, len(l)-1)

print(f4([1, 2, 3, 4], 5))
# 1.3.4 算法设计模式-算法思想-回溯
# 回溯是一种选优搜索法, 又称试探法, 当探索到某一步时, 发现原先选择不优或达不到目标, 就退回一步重新选择
# 回溯法解题思路: (1)定义解空间 (2)确定易于搜索的解空间结构 (3)以深度优先搜索解空间, 不合适则回溯, 注意是深度优先
"""用状态空间树的思维去理解, 从根节点出发, 回溯法不断地去试下一个子节点, 到了下一个子节点才知道上一个选的对不对"""
"""注意, 用回溯法的解是根节点到叶节点的路径, 而不是叶节点, 因为只有解的各个部分是逐步生成的, 才能中途发现不满足后回退一步"""
# 0-1背包问题, 给定n种物品和一背包, 物品i的重量为[3, 5, 2, 1], 价值分别为[9, 10, 7, 4], 背包容量7
# 问如何装背包使得总价值最大?定义解空间, 向量[1, 0, 1, 0]表示物品i选不选, 解空间可以是2叉树
# 除了根节点, 每一层表示每个物品选不选
def f5():
    w = [1, 2, 3, 5]
    v = [4, 7, 9, 10]  # 默认按单位重量价值由高到低排序, 便于演示限界函数
    n = 4
    c = 7
    s = [False for _ in range(n)]

    bestV = 0
    bestS = None

    # 注意界限函数的思路, 优先单位价值大的, 比如单位价值由高到低还是d e f 3个物品
    # 如果d能装进去就装, 剩下的空间看e能不能装进去, 能装就装, 装不进去则把e打碎了装进去
    # 这里的最优解是估算最优解, 不是实际准确的最优解, 不然这个函数不就能直接用于找全局最优解了吗
    # 既然是估算, 就要权衡性能和准确度, 不可能完全准确的
    # 另外, 这里的界限函数实际上是用到了贪心的思路
    def bound(i, curW, curV):
        lw = c - curW
        cv = curV

        while i < n and w[i] <= lw:
            lw -= w[i]
            cv += v[i]
            i += 1
        # 循环出来的i, 要么超限, 要么是装不下的那个, 后一种如要打碎了装进去
        if i < n:
            cv += (v[i]/w[i]) * lw
        return cv

    # 注意观察回溯法递归函数的结构
    def rf(i, curW, curV):
        nonlocal bestV, bestS
        # 叶节点也处理完了, 该判断要不要保留这个解了
        if i > n-1:
            if curV > bestV:
                bestV = curV
                bestS = s[:]
        else:
            # 如果还没处理完所有节点, 则枚举当前节点的可选值
            for each in [True, False]:
                s[i] = each
                cw = curW + (w[i] if s[i] else 0)
                cv = curV + (v[i] if s[i] else 0)
                # 利用约束函数和限界函数决定是否还往下走
                # 这里才是回溯法的精髓, 不然就变成递归形式的暴力法了
                # 约束函数一般和解本身无关, 而是外在添加的约束
                # 限界函数则表明当前解已经不符合要求了, 没必要继续往下走了
                # 最关键的, 怎么知道走一半的解没必要继续往下走???
                # 这里不考虑那些复杂的逻辑, 仅添加一种最简单的限界, 即超重了
                # 即限界函数为, 当前重量小于等于背包容量, 才继续往子节点走
                # 当然, 界限函数可以更复杂些, 比如, 加入物品是按单位价值倒排的
                # 假设处理完当前节点, 还剩x重量的空间没用, 提前估算出按当前路径走下去的最优解
                # 如果这个估算最优解小于全局最优解, 那么就没必要继续走下去了
                if cw <= c and bound(i+1, cw, cv) > bestV:
                    rf(i+1, cw, cv)
    rf(0, 0, 0)
    print(bestS, bestV)

f5()


# 1.3.5 算法设计模式-算法思想-分支限界
# 与回溯法有点类似, 区别在于, 回溯法要找出解空间中所有满足约束条件的解(比如上面的例子, 必须找出所有
# 解才能知道哪个是最好的), 而分支限界则是找出满足约束条件的一个解或某种意义下的最优解; 第二个区别是
# 回溯法以深度优先搜索解空间, 而分支限界法则以广度优先或最小耗费优先的方式搜索解空间; 第三个区别,
# 回溯法, 如果当前扩展节点不能够再往深度移动, 则当前扩展节点成为死节点, 此时回溯至最近一个活节点
# 处, 而分支界限法中, 每个活结点只有一次机会成为扩展节点, 活结点一旦成为扩展节点, 就一次性产生其
# 所有子节点, 一般用队列实现广度优先搜索. 关于第一点区别, 没太明白, 感觉分支限界和回溯的唯一区别
# 就是一个是深度一个是广度, 也都是在所有解里找最优, 而且也都存在限界函数, 还如叫深度限界, 广度限界
"""用状态空间树的思维去理解, 从根节点出发, 分支限界法不断地去试其所有子节点, 差不多就加到队列里去"""
"""注意, 用分支法的解也是根节点到叶节点的路径, 而不是叶节点"""
from collections import deque
def f6():
    w = [1, 2, 3, 5]
    v = [4, 7, 9, 10]
    n = 4
    c = 7

    # 分支限界用的是队列存储当前W, V
    bestV = 0
    bestS = None

    dq = deque()

    def bound(i, curW, curV):
        lw = c - curW
        cv = curV

        while i < n and w[i] <= lw:
            lw -= w[i]
            cv += v[i]
            i += 1
        # 循环出来的i, 要么超限, 要么是装不下的那个, 后一种如要打碎了装进去
        if i < n:
            cv += (v[i]/w[i]) * lw
        return cv

    # 压入初始节点
    for each in [True, False]:
        cw = w[0] if each else 0
        cv = v[0] if each else 0

        if cw <= c and bound(1, cw, cv) > bestV:
            dq.append((0, cw, cv, [each]))

    while dq:
        i, cw, cv, s = dq.popleft()

        i = i+1

        if i > n-1:
            if cv > bestV:
                bestV = cv
                bestS = s
        else:
            for each in [True, False]:
                cw2 = cw + (w[i] if each else 0)
                cv2 = cv + (v[i] if each else 0)
                # 处理完当前节点不超重且继续走下去可能最佳大于当前最佳
                # 才把当前节点入队列
                if cw2 <= c and bound(i+1, cw2, cv2) > bestV:
                    dq.append((i, cw2, cv2, s+[each]))

    print(bestS, bestV)

f6()


# 1.3.6 算法设计模式-算法思想-贪心
# 贪心指对问题求解时, 总是做出在当前看来最好的选择, 其得到的只是某种意义上的局部最优解而非整体最优
# 为了保证局部最优就是整体最优, 在用贪心法时, 需要问题具备贪心选择性质, 即一个问题的整体最优解可以
# 通过一系列局部的最优解的选择达到, 并且每次的选择可以依赖以前做出的选择, 但不依赖后面要做出的选择
# 换一种说法就是, 一个问题的最优解包含子问题的最优解, 即具有最优子结构性质
# 贪心算法没有固定的算法框架, 其设计的关键是贪心策略的选择; 注意, 贪心算法适用的情况很少
# 以背包问题为例, 传统的背包问题是不能用贪心的, 必须是物品可分隔, 然后贪心策略为优先选取单位价值最大
"""用状态空间树的思维去理解, 贪心算法需要满足这样的性质, 其子问题的最优解路径与整体最优解路径重合"""
"""比如n-1的最优解路径A-C-D-G, 那么n的最优解路径只能在此基础上扩展A-C-D-G-XXX"""
def f7():
    # 例子, 找零, 典型的贪心算法
    # 贪心策略, 每一步尽可能用面值大的
    # 100 50 20 10 5 2 1
    # 怎么证明这种贪心策略具有贪心选择性质呢?
    f = [100, 50, 20, 10, 5, 2, 1]
    p = 827
    r = {}
    for each in f:
        r[each] = p // each
        p = p % each
    print(r)
f7()

# 1.3.7 算法设计模式-算法思想-动态规划
# 动态规划类似于分治法, 也是将待求解问题分解成若干个子问题, 先求解子问题, 然后进一步得到原问题的解
# 硬要说区别的话, 分治法里分解完之后, 各个子问题是独立的(或者说解空间树里最终解是叶节点)
# 而动态规划里子问题往往不是相互独立的(解空间树里解一般是根节点到叶节点的路径, 而不是叶节点)
# 由于这种不相互独立, 中间节点会经过多次, 动态规划的思路就是把中间节点的值存起来, 避免重复计算
# 适用于动态规划的一般称为多阶段决策问题, 即一类活动可以分为若干个相互联系的阶段, 每一个阶段都
# 需要作出决策, 一个阶段的决策确定以后, 常常影响到下一个阶段的决策, 从而完全确定了一个过程的活动路线
# 各个阶段的决策构成一个决策序列, 称为一个策略
# 要求状态满足无后效性, 即给定某一阶段的状态, 则再这一阶段以后过程的发展不受这阶段以前各阶段状态的影响
# 即每个阶段选择策略时只需考虑当前的状态, 而无需考虑过程的历史

# 适用动态规划的问题需要满足1. 最优化原理, 即最优子结构, 不论过去状态和决策如何, 对前面的决策所形成的状态
# 而言, 余下的诸策略必须构成最优策略; 2. 无后效性, 以前各阶段的状态无法影响未来的决策; 3. 子问题有重叠性
# 贪心是一条路走到黑, 动规是中间状态都求出来

from collections import deque
def f8():
    # 还是0-1背包问题
    """
    1. 先抽象问题, max(aV1+bV2+....), a..b..取值0或1
    约束条件, aW1+bW2+... <= capacity
    2. 能不能用动态规划, 要证明是否满足最优化原理, 用反证法
    (a, b, c...)为最优解, 假设(b, c...)不是子问题最优, 而是(m, n....)
    则: aV1+mV2+nV3+... > aV1+bV2+cV3...
    那么原问题的最优解就是(a, m, n...)了而不是(a, b, c...), 假设不成立
    所以(b, c, ...)是子问题最优解
    所以该问题满足最优化原理
    3. 定义V(i, j), 表示在前i个物品挑选总重量不超过j的物品的最优值
    寻找递推关系式, 对于第i个物品
    (1) j < w(i), V(i, j) = V(i-1, j)
    (2) j > w(i), V(i, j) = max(V(i-1, j), V(i-1, j-w(i))+v(i))
    !!!动规最关键的就是想出来这么个表格, 可以是一维, 也可以是二维的!!!
    怎么理解这俩递推关系式?
    比如V(4, 7)? 7能装下第四个物品, 所以V(4, 7)的最优值有两种路径, 选第4个和不选第4个
    即: max V(3, 7-5)+10 和 V(3, 7)

    按行去遍历, 每一行的意义为前i个物品, 背包容量分别为1~7时最优解(其实有点像暴力枚举...)

    4. 初始化边界, V(x, 0)肯定为0, 即第一竖列都为0, V(0, y), 还没开始装, 也都是0

    """
    w = [0, 1, 2, 3, 5]
    v = [0, 4, 7, 9, 10]  # w, v前面补俩0便于操作
    n = 4
    c = 7
    np = [[0 for _ in range(c+1)] for _ in range(n+1)]
    res = [False for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, c+1):
            if w[i] > j:
                np[i][j] = np[i-1][j]
            else:
                np[i][j] = max(np[i-1][j], np[i-1][j-w[i]]+v[i])
    print(np[4][7])  # 20
    print(np)
    # 求出来最优解的值之后, 还要往回找, 找到其对应的多阶段决策
    ct = 7
    for i in range(n, 0, -1):
        if np[i][ct] == np[i-1][ct]:
            res[i] = False
        else:
            res[i] = True
            ct -= w[i]
    print(res[1:])
f8()

def f9():
    # 动规例题2, 斐波那契竖列 f(n) = f(n-1) + f(n-2)
    """
    判断条件:
    1. 判断特征有最优子结构
    2. 子问题间有重叠(存储中间结果, 节约计算)

    一般过程:
    1. 发现子问题
    2. 确定状态转移方程 f(n) = f(n-1) + f(n-2)
    """
    # 递归形式
    n = 10
    dp = [-1 for _ in range(n+1)]
    dp[1], dp[2] = 0, 1

    def rf(n):
        v1, v2 = None, None
        if dp[n-1] == -1:
            dp[n-1] = v1 = rf(n-1)
        else:
            v1 = dp[n-1]
        if dp[n-2] == -1:
            dp[n-2] = v2 = rf(n-2)
        else:
            v2 = dp[n-2]
        return v1+v2

    print(rf(10))

    # 非递归形式
    dp = [-1 for _ in range(n+1)]
    dp[1], dp[2] = 0, 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[10])

f9()


"""软件工程设计模式"""
# 2.1.1 软件工程设计模式-创建型模式-工厂, Factory Method
# 简单工厂, 创建一个工厂类, 用于实例化对象
# 简单工厂生产模式固定, 比如一共三种产品
# 某工厂生产两种, 那这个两种就固定了, 即createPizza方法固定, 可以理解为生产线
from abc import ABCMeta, abstractmethod
class Pizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self):
        pass

class CheesePizza(Pizza):
    def prepare(self):
        print("prepare cheese pizza")

class PepperPizza(Pizza):
    def prepare(self):
        print("prepare pepper pizza")

class GreekPizza(Pizza):
    def prepare(self):
        print("prepare greek pizza")

class PizzaFactory:
    def createPizza(self, ptype):
        if ptype == 'cheese':
            return CheesePizza()
        elif ptype == 'pepper':
            return PepperPizza()
        else:
            return None
pizza_factory = PizzaFactory()
pizza = pizza_factory.createPizza("cheese")
pizza.prepare()

# 工厂模式, 在简单工厂基础上, 对createPizza方法进一步抽象
# 可以在现有产品基础上, 任意组件生产线, 支持生产其中的某种或某几种产品
# 抽象工厂模式则是在工厂模式的基础上, 把多种工厂再封起来, 称为返回工厂的工厂
class BaseFactory(metaclass=ABCMeta):
    @abstractmethod
    def createPizza(self, ptype):
        pass

# 生产线1, 只生产cheese和pepper, cheese和pepper归属于同一产品线
class FirstFactory(BaseFactory):
    def createPizza(self, ptype):
        if ptype == 'cheese':
            return CheesePizza()
        elif ptype == 'pepper':
            return PepperPizza()
        else:
            return None
# 生产线2, 只生产cheese和greek
class SecondFactory(BaseFactory):
    def createPizza(self, ptype):
        if ptype == 'cheese':
            return CheesePizza()
        elif ptype == 'greek':
            return GreekPizza()
        else:
            return None

factory = SecondFactory()
pizza = factory.createPizza("greek")
pizza.prepare()


# 2.1.2 软件工程设计模式-创建型模式-抽象工厂, Abstract Factory
# 抽象工厂, 在工厂的基础上在进一步抽象, 不仅可以自定义单个产品系列的产品线
# 还可以支持增加其他产品系列的产品线
# 比如不光有三种pizza, 还有三种馅饼, fruit, bean, veg
# 其实如果不添加其他各种中间抽象类, 抽象工厂模式和工厂模式唯一区别在于
# BaseFactory里有多个产品序列而不是一个, 当然一个的时候也是抽象工厂模式
# 即工厂模式是一种特殊的抽象工厂模式
class Pizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self):
        pass

class CheesePizza(Pizza):
    def prepare(self):
        print("prepare cheese pizza")

class PepperPizza(Pizza):
    def prepare(self):
        print("prepare pepper pizza")

class GreekPizza(Pizza):
    def prepare(self):
        print("prepare greek pizza")

class Cake(metaclass=ABCMeta):
    @abstractmethod
    def cook(self):
        pass
class FruitCake(Cake):
    def cook(self):
        print("cook fruit cake")
class BeanCake(Cake):
    def cook(self):
        print("cook bean cake")
class VegCake(Cake):
    def cook(self):
        print("cook veg cake")

# 两个系列的产品, 每个系列三种

class BaseFactory(metaclass=ABCMeta):
    @abstractmethod
    def createPizza(self):
        pass
    @abstractmethod
    def createCake(self):
        pass

# A工厂支持生产第一种pizza和第一种cake
class AFactory(BaseFactory):
    def createPizza(self):
        return CheesePizza()

    def createCake(self):
        return FruitCake()

# B工厂支持生产第二种pizza和第三种cake
class BFactory(BaseFactory):
    def createPizza(self):
        return PepperPizza()

    def createCake(self):
        return VegCake()

factory = AFactory()
pizza = factory.createPizza()
pizza.prepare()
cake = factory.createCake()
cake.cook()
# 除了上面的普通抽象工厂, 还可以再添加一个中间层PizzaFactory, CakeFactory

# 有些地方说抽象工厂不只是多个条线, 而且在工厂上层还多了一个工厂的工厂
# 到底哪种才是抽象工厂的定义呢?
class FactoryBuilder:
    def buildFactory(self, ftype):
        if ftype == 'a':
            return AFactory()
        if ftype == 'b':
            return BFactory()


# 2.1.3 软件工程设计模式-创建型模式-单例, Singleton
# 单例类自己创建自己唯一实例, 其他对象要用的时候判断该单例是否已存在, 存在返回没有创建
# python里没办法把构造函数声明为私有, 所有得利用__new__, 拦截默认创建方法
# __new__是在实例创建前被调用的, 是个静态方法, 其主要作用是创建实例并返回实例对象
# __init__是对象创建完成后调用的, 其主要是设置对象属性的一些初始值, 是个实例方法
class Single:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    # 这里是在init里给实例变量赋值还是在new里直接赋值
    # 看新的o=Single(xxx)是否要改变变量的值
    # 如果要变, 建议写__init__函数, 不变, 直接在new里赋值
    # 当然, 变这种情况也是能在new里赋值的, 取到原对象后改变变量值就是
    def __init__(self, x=None):
        if x: self.x = x


o1 = Single(100)
print(id(o1), o1.x)
o2 = Single(200)
print(id(o2), o2.x)  # 这俩id是一样的
o3 = Single()
print(id(o3), o3.x)

# 2.1.4 软件工程设计模式-创建型模式-建造者, Builder
# 将一个复杂对象的构建与它的表示分离, 使得同样的构建过程可以创建不同的表示
# 即使用多个简单的对象一步一步构建成一个复杂的对象
# 如果将抽象工厂模式看成汽车配件生产工厂, 那么建造者模式就是一个汽车组装工厂
# 通过对部件的组装可以返回一辆完整的汽车
class Bike:
    def __init__(self):
        self.frame = None
        self.seat = None

class Frame(metaclass=ABCMeta):
    @abstractmethod
    def getInfo(self):
        pass
class AlloyFrame(Frame):
    def getInfo(self):
        print("alloy frame")
class IronFrame(Frame):
    def getInfo(self):
        print("iron frame")

class Seat(metaclass=ABCMeta):
    @abstractmethod
    def getInfo(self):
        pass

class WoodSeat(Seat):
    def getInfo(self):
        print("wood seat")

class PlasticSeat(Seat):
    def getInfo(self):
        print("plastic seat")

class Builder(metaclass=ABCMeta):
    @abstractmethod
    def buildFrame(self):
        pass
    @abstractmethod
    def buildSeat(self):
        pass

class ForeverBuilder(Builder):
    def __init__(self):
        self.bike = Bike()

    def buildFrame(self):
        self.bike.frame = AlloyFrame()

    def buildSeat(self):
        self.bike.frame = PlasticSeat()

    def getBike(self):
        return self.bike

class OfoBuilder(Builder):
    def __init__(self):
        self.bike = Bike()

    def buildFrame(self):
        self.bike.frame = IronFrame()

    def buildSeat(self):
        self.bike.frame = WoodSeat()

    def getBike(self):
        return self.bike

# Director不是必须的, 直接到Builder一级就行
# 到Builder一级的话, Builder在自己的__init__里调buildFrame和buildSeat就行
class Director:
    def __init__(self, btype):

        if btype == 'forever':
            self.builder = ForeverBuilder()
        else:
            self.builder = OfoBuilder()

    def construct(self):
        self.builder.buildFrame()
        self.builder.buildSeat()
        return self.builder.getBike()

director = Director("forever")
bike = director.construct()
bike.frame.getInfo()
# 2.1.5 软件工程设计模式-创建型模式-原型, Prototype
# 用于创建当前对象的克隆; 深拷贝用到copy
# 目的是减少个别数据的初始化, 仅更新部分数据
import copy
class ProtoType:
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(kwargs)
        return obj

class A:
    def __init__(self):
        self.x = 100

a = A()
print(a.x)  # 100

prototype = ProtoType()
prototype.register('a', a)

b = prototype.clone('a', x=1000, y=200)

print(b.x, b.y)  # 1000, 200

# 2.2.1 软件工程设计模式-结构型模式-适配器, Adapter
# 将一个类的接口转换成客户希望的另外一个接口, 使得原本由于接口不兼容而不能在一起工作的那些类可以一起工作
# 适配方法可以在适配器里做兼容, 也可以外部传入
class Dog:
    def bark(self):
        print("dog bark")

    def f(self):
        print("dog fprint")

class Cat:
    def meow(self):
        print("cat meow")

class Adapter1:
    def __init__(self, obj):
        self._obj = obj

    def make_sound(self):
        if isinstance(self._obj, Dog):
            self._obj.bark()
        if isinstance(self._obj, Cat):
            self._obj.meow()
dog = Dog()
adapter = Adapter1(dog)
adapter.make_sound()
cat = Cat()
adapter = Adapter1(cat)
adapter.make_sound()

# 第二种办法, 外部传
class Adapter2:
    def __init__(self, obj, **method_map):
        self.obj = obj
        self.__dict__.update(method_map)

    # 注意这里要用__getattr__, 找不到时才去obj里找
    def __getattr__(self, item):
        return getattr(self.obj, item)

dog = Dog()
adapter = Adapter2(dog, make_sound=dog.bark)
adapter.make_sound()
adapter.f()

# 2.2.2 软件工程设计模式-结构型模式-装饰器, Decorator
# 有点像mixin, 给类添加功能组件, 区别于descriptor/property
# 不过和mixin也是有点区别的, 装饰器是直接写, 而mixin是先把装饰的部分独立成组件类, 然后再混入

class A:
    def __init__(self):
        self.x = 100

# 装饰器
class KeyDecorator:
    def __init__(self, obj):
        self._obj = obj

    def __getitem__(self, item):
        return self._obj.__dict__.get(item)

    def __getattr__(self, item):
        return getattr(self._obj, item)

a = A()
key_decorator = KeyDecorator(a)
print(a.x, key_decorator.x, key_decorator['x'])

# mixin
# 感觉装饰器像是临时附魔, 比如这次赋予武器暴击效果
# mixin则是直接创造一种新的自带暴击效果的武器类型
class ComponentKey:
    def __getitem__(self, item):
        return self.__dict__.get(item)

class MixinA(A, ComponentKey):
    pass

a = MixinA()
print(a.x, a['x'])


# 2.2.3 软件工程设计模式-结构型模式-代理, Proxy
# 一个类代表另一个类的功能, 不直接使用目标对象, 而是通过A使用B
import time
class SalesManager:
    def work(self):
        print("sales manager working")
    def talk(self):
        print("sales manager talking")

class Proxy:
    def __init__(self):
        self.busy = 'No'
        self.sale = None
    def work(self):
        print("Proxy checking for sales manager availability")
        if self.busy == 'No':
            self.sale = SalesManager()
            time.sleep(0.2)
            self.sale.talk()
        else:
            time.sleep(0.2)
            print("sales manager is busy")

p = Proxy()
p.work()
p.busy = 'Yes'
p.work()

# 2.2.4 软件工程设计模式-结构型模式-外观, Facade
# 为子系统中的一组接口提供一个一致的界面, 比如pygame里的group?
class TC1:
    def run(self):
        print("running TC1")

class TC2:
    def run(self):
        print("running TC2")

class Facade:
    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tcs = [self.tc1, self.tc2]

    def runAll(self):
        for each in self.tcs: each.run()

f = Facade()
f.runAll()


# 2.2.5 软件工程设计模式-结构型模式-桥接, Bridge
# 将抽象部分与实现部分分离, 使它们都可以独立地变化
# 感觉有点像适配器的第二种实现, 都是外传一些方法, 以实现动态绑定
class DrawAPI1:
    def draw(self):
        print("api1 draw circle")

class DrawAPI2:
    def draw(self):
        print("api2 draw circle")

class DrawCircle:
    def __init__(self, draw_api):
        self.draw_api = draw_api

    def draw(self):
        self.draw_api.draw()

dc = DrawCircle(DrawAPI1())
dc.draw()

# 2.2.6 软件工程设计模式-结构型模式-组合, Composite
# 区别于fishc里提到的类的组合, 那个仅仅只是一个类里的变量类型是自定义类类型
# 而这里的组合要求更高, 一个类兼具部分整体的特性,依据树形结构来组合对象
class Employee:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        # 这里children列表的元素类型是Employee本身
        self.children = []

    def add(self, obj):
        self.children.append(obj)

    def remove(self, obj):
        self.children.remove(obj)

    def getChildren(self):
        return self.children

    def __str__(self):
        return "Name: {}, Pos: {}".format(self.name, self.pos)

ceo = Employee("John", "CEO")
headSale = Employee("Robert", "Head Sale")
headMarket = Employee("Michel", 'Head Market')
ceo.add(headSale)
ceo.add(headMarket)

sale1 = Employee("Jim", "Sale")
sale2 = Employee("Lucy", "Sale")
headSale.add(sale1)
headSale.add(sale2)

market1 = Employee("Tom", "Market")
market2 = Employee("Eric", "Market")
headMarket.add(market1)
headMarket.add(market2)

def rf(obj):
    if not obj:
        return
    print(obj)
    for each in obj.getChildren():
        rf(each)
rf(ceo)
# 2.2.7 软件工程设计模式-结构型模式-享元, Flyweight
# 进阶版的单例模式, 只不过是多个(类似单例, 可以通过获取对象方法实现, 也可以改写__new__)
# 如果有相同的业务请求, 则尝试重用现有的同类对象, 如果未找到则创建
# 至于存储对象列表有两种办法, 一种是dict强映射, 一种是用weakref弱映射
# weakref与dict类似, 只不过dict里的对象会保持存活, 而weakref里的映射对象
# 如果没有其他强引用时, 垃圾回收机制可以回收该对象并将其在弱映射对象中相应的条目删除

# 第一种实现方式
class Circle:
    def __init__(self, color):
        self.color = color

    def draw(self):
        print("draw circle with color {}".format(self.color))

# 其实这里没必要用简单工厂, 因为只有一种类, 只是color取值不同而已
# 可以直接把对象dict存到Circle的类变量里去
class CircleFactory:
    def __init__(self):
        self.circles = {}

    def getCircle(self, color):
        if color in self.circles:
            return self.circles.get(color)
        else:
            circle = Circle(color)
            self.circles[color] = circle
            return circle

cf = CircleFactory()
c1 = cf.getCircle("red")
c1.draw()
c2 = cf.getCircle("blue")
c2.draw()
c3 = cf.getCircle("red")
print(c1 is c3)

import weakref
# 第二种实现方式, 改写__new__, 并尝试用一下weakref
# 注意如果有多种类对象, 那这里就不能直接在原对象上改写了, 得单独出来个factory改写
class Shape:
    _pool = weakref.WeakValueDictionary()

    def __new__(cls, color):
        if color in cls._pool:
            return cls._pool.get(color)
        else:
            obj = super().__new__(cls)
            cls._pool[color] = obj
            obj.color = color
            return obj

    def getColor(self):
        print(self.color)
    # 这里不要写init了, init里无法判断是老对象还是新创建的对象
    # 会导致重复操作, 不如直接在new里赋值
    # def __init__(self, color):
        # self.color = color

s = Shape("yellow")
s2 = Shape("blue")
s3 = Shape("yellow")
print(id(s), id(s2), id(s3))

# 2.3.1 软件工程设计模式-行为型模式-策略, Strategy
# 定义一系列的算法, 把他们一个个封装起来, 并且使它们可以互相替换
# 比如sort时的key值函数?
# 这里的算法支持类内定义, 也可以外部传
import types
class Strategy:
    def __init__(self, strategy):
        self.execute = self.s
        if strategy == 's1':
            self.execute = self.s1
        if strategy == 's2':
            self.execute = self.s2
        # types.MethodType(f, obj)可以把外部方法绑定到对象上
        if callable(strategy):
            self.execute = types.MethodType(strategy, self)
            # 也可以这么写
            # self.execute = lambda :strategy(self)

    def s(self):
        print("缺省算法")
    def s1(self):
        print("内置算法1")

    def s2(self):
        print('内置算法2')

def sout(self):
    print("外部绑定", self)

s = Strategy("s1")
s.execute()
s = Strategy(sout)
s.execute()

# 2.3.2 软件工程设计模式-行为型模式-模板, Template
# 一个抽象类公开定义了执行它的方法的方式/模板, 子类可以按需要重写方法实现, 但调用将以抽象类中定义的方式进行
# 即比普通的抽象类多定义了点东西, 制定了一个算法的框架, 子类可以可以重写该算法的各个部分
# 利用抽象类特性, 制定顶层逻辑框架, 将逻辑的细节以抽象方法的形式强制子类去实现
class SortTemplate(metaclass=ABCMeta):
    def __init__(self):
        self.l = [4, 3, 2, 1]

    @abstractmethod
    def sort(self):
        pass
    @abstractmethod
    def fout(self):
        pass

    # 模板里定义了算法的框架, 但对于算法的某些关键步骤, 采用的是抽象方法, 需要子类去实现
    def play(self):
        self.sort()
        self.fout()

class MySort(SortTemplate):
    def sort(self):
        print("开始排序")
    def fout(self):
        print(self.l)

ms = MySort()
ms.play()
# 2.3.3 软件工程设计模式-行为型模式-观察者, Observer
# 当一个对象被修改时, 自动通知依赖它的对象, 而并不知道有多少依赖它, 有点像react里的state
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        for each in self._observers:
            each.update(self)

# Target其实可以和Subject合并成一个类, 不过为了避免重写Subject, 一般不放一块
class Target(Subject):
    def __init__(self):
        super().__init__()
        self._data = 8

    def getData(self):
        return self._data

    def setData(self, value):
        self._data = value
        self.notify()

    data = property(getData, setData)

class DataChangeObserver:
    def update(self, target):
        print("检测到目标值改动", target.data)

class DataZeroObserver:
    def update(self, target):
        if target.data == 0:
            print("警告, data值变成0了")
# 可以添加多个observer, 以针对不同的改动进行不同的处理
t = Target()
t.attach(DataChangeObserver())
t.attach(DataZeroObserver())
print(t.data)
t.data = 100
t.data = 0

# 2.3.4 软件工程设计模式-行为型模式-访问者, Visitor, 最复杂的设计模式
# 元素对象接受访问者对象, 从而访问者对象可以处理元素对象上的操作, 主要是为了将数据结构和数据操作分离
# 适用场景: 对象结构比较稳定, 但经常需要在对象上定义新的操作, 不希望这些操作污染原对象的类
# visitor, 抽象类, 定义对每个element的访问行为, 有几个元素就有几个方法, 所以该模式要求元素结构不经常改变
# concretevisitor, 具体的访问者
# element, 元素抽象类, 定义了一个接受访问者的方法
# elementA, elementB, 具体的元素类
# objectstructure, 定义对象结构, 并且可以迭代这些元素提供访问者访问

# 示例, 员工分为工程师和经理, 年终考核CEO和CTO分别关注不同方面, CTO关注工程师代码量, 经理的新产品数量
# CEO关注工程师的KPI和经理的KPI以及新产品数量
# element
import random
class Staff(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self.kpi = random.randint(1, 10)

    def accept(self, visitor):
        pass

# elementA
class Engineer(Staff):
    def __init__(self, name):
        super().__init__(name)
        self.code = random.randint(1, 100000)

    def accept(self, visitor):
        visitor.visit(self)

# elementB
class Manager(Staff):
    def __init__(self, name):
        super().__init__(name)
        self.product = random.randint(1, 10)

    def accept(self, visitor):
        visitor.visit(self)

# object structure
class BusinessReport:
    def __init__(self):
        self.staffs = []
        self.staffs.append(Manager("经理-A"))
        self.staffs.append(Engineer("工程师-A"))
        self.staffs.append(Engineer("工程师-B"))
        self.staffs.append(Manager("经理-B"))
        self.staffs.append(Engineer("工程师-C"))

    def showReport(self, visitor):
        for each in self.staffs:
            each.accept(visitor)

class Visitor(metaclass=ABCMeta):
    def visit(self, staff):
        pass

# python里没有重载, 没办法写俩visit, 如果elementA和elementB有各自个性化的东西, 就不好办了
class CEOVisitor(Visitor):
    def visit(self, staff):
        if isinstance(staff, Manager):
            print("经理: {}, KPI: {}, 产品数量: {}".format(staff.name, staff.kpi, staff.product))
        if isinstance(staff, Engineer):
            print("工程师: {}, KPI: {}".format(staff.name, staff.kpi))

class CTOVisitor(Visitor):
    def visit(self, staff):
        if isinstance(staff, Manager):
            print("经理: {}, 产品数量: {}".format(staff.name, staff.product))
        if isinstance(staff, Engineer):
            print("工程师: {}, 代码量: {}".format(staff.name, staff.code))

report = BusinessReport()
print("=====CEO报表=====")
report.showReport(CEOVisitor())
print("=====CTO报表=====")
report.showReport(CTOVisitor())

# 2.3.5 软件工程设计模式-行为型模式-中介者, Mediator
# 降低多个对象和类之间的通信复杂性, 并支持松耦合
class ChatRoom:
    @staticmethod
    def send(user, message):
        print("[{}]: {}".format(user.name, message))

class User:
    def __init__(self, name):
        self.name = name

    def sendMessage(self, message):
        ChatRoom.send(self, message)

robert = User("Robert")
john = User("John")

robert.sendMessage("hi, John~")
john.sendMessage("Nice to meet you too")

# 2.3.6 软件工程设计模式-行为型模式-迭代器, Iterator
# 两种方式, 传统方式和用yield方式(即generator), 推荐后者
class Iterator(metaclass=ABCMeta):

    def hasNext(self) -> bool:
        return

    def next(self) -> object:
        pass


class MyClass(Iterator):
    def __init__(self):
        self.l = [8, 100, 7, 2, 0]
        self.i = 0

    def hasNext(self) -> bool:
        if self.i < len(self.l):
            return True
        return False

    def next(self) -> object:
        self.i += 1
        return self.l[self.i-1]

m = MyClass()
while m.hasNext():
    print(m.next())

# 或者更简单的方式
class MyGenerator:

    def __init__(self):
        self.l = [8, 100, 7, 2, 0]

    def generator(self):
        for each in self.l:
            yield each

mg = MyGenerator()
for each in mg.generator():
    print(each)

# 2.3.7 软件工程设计模式-行为型模式-责任链, Chain of Responsibility
# 为请求创造一个接受者的对象的链, 如果一个对象不能处理该请求, 那么它会把相同的请求传给下一个接收者
class ChainHandler:
    def nextHandler(self, obj):
        self.next_handler = obj

class Handler1(ChainHandler):
    def handle(self, request):
        if 0 < request <= 10:
            print("in handle1")
        else:
            self.next_handler.handle(request)

class Handler2(ChainHandler):
    def handle(self, request):
        if 10 < request <= 20:
            print("in handle2")
        else:
            self.next_handler.handle(request)

class Handler3(ChainHandler):
    def handle(self, request):
        if 20 < request <= 30:
            print("in handle3")
        else:
            print("end of chain")

h1 = Handler1()
h2 = Handler2()
h3 = Handler3()
h1.nextHandler(h2)
h2.nextHandler(h3)

request = [2, 5, 14, 40, 22, 18, 3, 35]
for each in request:
    h1.handle(each)
# 2.3.8 软件工程设计模式-行为型模式-命令, Command
# 请求以命令的形式包裹在对象中, 并传给调用对象, 调用对象寻找可以处理该命令的合适的对象, 并把
# 该命令传给相应的对象
class Stock:
    def __init__(self):
        self.name = 'abc'
        self.quantity = 10

    def buy(self):
        print("Stock {} bought with quantity {}".format(self.name, self.quantity))

    def sell(self):
        print("Stock {} sold with quantity {}".format(self.name, self.quantity))

# 命令这里封装一层是为了Broker里可以统一行为
class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class Order1(Order):
    def __init__(self, block: Stock):
        self.block = block

    def execute(self):
        self.block.buy()

class Order2(Order):
    def __init__(self, block: Stock):
        self.block = block

    def execute(self):
        self.block.sell()

# 命令调度器, 经纪人
class Broker:
    def __init__(self):
        self.order_list = []

    def addOrder(self, order: Order):
        self.order_list.append(order)

    def executeOrders(self):
        for each in self.order_list:
            each.execute()
        self.order_list.clear()

stock = Stock()
order1 = Order1(stock)
order2 = Order2(stock)

broker = Broker()
broker.addOrder(order1)
broker.addOrder(order2)

broker.executeOrders()

# 2.3.9 软件工程设计模式-行为型模式-备忘录, Memento
# 保存一个对象的某个状态, 以便在适当的时候恢复对象, 有点像undo, redo
import copy
class Memento:
    def __init__(self, obj: object, deep=False):
        self.state = (copy.copy, copy.deepcopy)[deep](obj.__dict__)

    def getState(self):
        return self.state

# 管理多个Memento
class CareTaker:
    def __init__(self):
        self.memento_list = []

    def add(self, memento: Memento):
        self.memento_list.append(memento)

    def get(self, index: int):
        return self.memento_list[index]

class Originator:
    def __init__(self, x):
        self.x = x

    def getMemento(self):
        return Memento(self)

    # 如果在Originator里restore, 那Memento里其实没必要存obj了
    # 只存个obj.__dict__就行
    def restoreFromMemento(self, memento: Memento):

        self.__dict__.clear()
        self.__dict__.update(memento.getState())

caretaker = CareTaker()

originator = Originator("state 1")
caretaker.add(originator.getMemento())

originator.x = "state 2"
caretaker.add(Memento(originator))  # 两种获取memento的写法都行

print(originator.x)  # state 2

originator.restoreFromMemento(caretaker.get(0))
print(originator.x)  # state 1


# 2.3.10 软件工程设计模式-行为型模式-状态, State ( Context )
# 在状态模式中, 类的行为是基于它的状态而改变的, 我们创建表示各种状态的对象和一个行为
# 随着状态对象改变而改变的context对象(后台接口一般采用这种模式, 共享上下文)

# context感觉不用外面传, 用单例模式, doAction里面自己获取就行
class State(metaclass=ABCMeta):
    def doAction(self, context):
        pass

class StartState(State):
    def doAction(self, context):
        print("state is start")
        context.setState(self)

class StopState(State):
    def doAction(self, context):
        print("state is stop")
        context.setState(self)

class Context:
    def __init__(self):
        self.state = None

    def setState(self, state: State):
        self.state = state

    def getState(self):
        return self.state

context = Context()

start = StartState()
start.doAction(context)
print(context.getState())

stop = StopState()
stop.doAction(context)
print(context.getState())

# 2.3.11 软件工程设计模式-行为型模式-解释器, Interpreter
# 实现一个表达式接口, 该接口解释一个特定的上下文, 常用于SQL解析, 运算符表达式, 编译器等
class Expression:
    def interpret(self, s: str):
        pass

class VarExpression(Expression):
    def __init__(self, key):
        self.key = key

    def interpret(self, d: dict):
        return d.get(self.key)

class AddExpression(Expression):
    def __init__(self, expr1: VarExpression, expr2: VarExpression):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, d: dict):
        return self.expr1.interpret(d) + self.expr2.interpret(d)

v1 = VarExpression("x")
v2 = VarExpression("y")
d = {"x": 100, "y": 200}

print(v1.interpret(d))

a1 = AddExpression(v1, v2)
print(a1.interpret(d))

# 补充1, 过滤器模式
# 使用不同的标准过滤一组对象, 通过逻辑运算以解耦的方式把它们连接起来, 将多个标准结合成一个标准
# 感觉和解释器模式有种神似

from typing import *
class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

class Criteria(metaclass=ABCMeta):
    def check(self, persons: List[Person]) -> List[Person]:
        pass

class MaleCriteria(Criteria):
    def check(self, persons: List[Person]) -> List[Person]:
        l = []
        for each in persons:
            if each.gender == 'MALE':
                l.append(each)

        return l

class AgeCriteria(Criteria):
    def check(self, persons: List[Person]) -> List[Person]:
        l = []
        for each in persons:
            if each.age >= 18:
                l.append(each)
        return l

class AndCriteria(Criteria):
    def __init__(self, c1: Criteria, c2: Criteria):
        self.c1 = c1
        self.c2 = c2

    def check(self, persons: List[Person]) -> List[Person]:
        return self.c2.check(self.c1.check(persons))

persons = list()
persons.append(Person("AAA", "MALE", 30))
persons.append(Person("BBB", "FEMALE", 13))
persons.append(Person("CCC", "FEMALE", 30))
persons.append(Person("DDD", "MALE", 8))
persons.append(Person("EEE", "MALE", 30))

c1 = MaleCriteria()
c2 = AgeCriteria()
c3 = AndCriteria(c1, c2)

print([e.name for e in c1.check(persons)])
print([e.name for e in c2.check(persons)])
print([e.name for e in c3.check(persons)])

# 补充2, 空对象模式
# 一般情况下, 用o==None判断空对象, 但有时候我们希望在这种情况下能做一些自定义操作
class Book(metaclass=ABCMeta):
    def isNone(self):
        pass
    def show(self):
        pass

class NormalBook(Book):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def isNone(self):
        return False

    def show(self):
        print("图书编号: {}, 书名: {}".format(self.id, self.name))

class NoneBook(Book):
    def isNone(self):
        return True

    def show(self):
        print("无效的图书信息!!!")

class BookFactory:
    def createBook(self, id):
        if id == 1:
            return NormalBook(1, "图书1")
        if id == 2:
            return NormalBook(2, "图书2")
        return NoneBook()
bf = BookFactory()
bf.createBook(1).show()
bf.createBook(-1).show()

# 补充3, MVC模式

# 补充4, 业务代表模式

# 补充5, 组合实体模式

# 补充6, 数据访问对象模式DAO

# 补充7, 前端控制器模式

# 补充8, 拦截过滤器模式

# 补充9, 服务定位器模式

# 补充10, 传输对象模式
