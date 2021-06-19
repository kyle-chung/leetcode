给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 

示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

思路与算法

由于我们需要求出所有和为 target 的组合，并且每个数只能使用一次，因此我们可以使用递归 + 回溯的方法来解决这个问题：

我们用 dfs(pos,rest) 表示递归的函数，其中 pos 表示我们当前递归到了数组 candidates 中的第 pos 个数
而 rest 表示我们还需要选择和为 rest 的数放入列表作为一个组合；

对于当前的第 pos 个数，我们有两种方法：选或者不选。
如果我们选了这个数，那么我们调用 dfs(pos+1,rest−candidates[pos]) 进行递归
注意这里必须满足 rest ≥ candidates[pos]。如果我们不选这个数，那么我们调用 dfs(pos+1,rest) 进行递归；

在某次递归开始前，如果 rest 的值为 0，说明我们找到了一个和为 target 的组合，将其放入答案中。
每次调用递归函数前，如果我们选了那个数，就需要将其放入列表的末尾，该列表中存储了我们选的所有数。
在回溯时，如果我们选了那个数，就要将其从列表的末尾删除。

上述算法就是一个标准的递归 + 回溯算法，但是它并不适用于本题。
这是因为题目描述中规定了解集不能包含重复的组合，而上述的算法中并没有去除重复的组合。

例如当 candidates=[2,2], target=2 时，上述算法会将列表 [2] 放入答案两次。

因此，我们需要改进上述算法，在求出组合的过程中就进行去重的操作。
我们可以考虑将相同的数放在一起进行处理，也就是说，如果数 x 出现了 y 次，那么在递归时一次性地处理它们
即分别调用选择 0, 1,⋯,y 次 x 的递归函数。这样我们就不会得到重复的组合。具体地：

我们还可以进行什么优化（剪枝）呢？
一种比较常用的优化方法是，我们将 freq 根据数从小到大排序，这样我们在递归时会先选择小的数，再选择大的数。
这样做的好处是，当我们递归到 dfs(pos,rest) 时
如果 freq[pos][0] 已经大于 rest，那么后面还没有递归到的数也都大于 rest
这就说明不可能再选择若干个和为 rest 的数放入列表了。
此时，我们就可以直接回溯。

# backtracking 时间复杂度：O(2^n * n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(pos: int, rest: int):
            nonlocal sequence
            if rest == 0:
                ans.append(sequence[:])
                return
            if pos == len(freq) or rest < freq[pos][0]:
                return
            
            dfs(pos + 1, rest)

            most = min(rest // freq[pos][0], freq[pos][1])
            for i in range(1, most + 1):
                sequence.append(freq[pos][0])
                dfs(pos + 1, rest - i * freq[pos][0])
            sequence = sequence[:-most]
        
        freq = sorted(collections.Counter(candidates).items())
        ans = list()
        sequence = list()
        dfs(0, target)
        return ans
















