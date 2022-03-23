import random, math

def ABP(std_id, min_v, max_v):
    depth = int(std_id[0])*2 #turns
    branch = int(std_id[2])
    init_hp = int(std_id[len(std_id)-1:len(std_id)-3:-1])

    print("Depth and branch ratio is " + str(depth)+':'+ str(branch))

    random_leaf_nodes = []
    tree = []

    for i in range(branch**depth):
        num = random.randint(min_v, max_v)
        random_leaf_nodes.append(num)

    print("Terminal States (leaf node values) are ",str(random_leaf_nodes)[1:-1])
    tree += random_leaf_nodes

    for i in range(depth):
            val = pow(branch, i)
            for j in range(val):
                if i%2!=0:
                    tree.append(math.inf)
                else:
                    tree.append(-math.inf)

    def alpha_beta_pruning(idx, alpha, beta, branch, depth, max_player):

        init_idx = branch*idx + 1
        stop_idx  = branch*idx + (branch+1)
        global node_visited

        if depth == 0:
            return tree[idx]

        if max_player:
            tree[idx] = -math.inf

            for i in range(init_idx, stop_idx):
                new_max_val = alpha_beta_pruning(i, alpha, beta, branch, depth - 1, False)
                alpha = max(alpha, new_max_val)
                tree[idx] = max(tree[idx], new_max_val)
                if beta <= alpha:
                    break #pruned
            return tree[idx]

        else:
            for i in range(init_idx, stop_idx):
                new_min_val = alpha_beta_pruning(i, alpha, beta, branch, depth - 1, True)
                beta = min(beta, new_min_val)
                tree[idx] = min(tree[idx], new_min_val)
                if depth == 1:
                    node_visited += 1
                if beta <= alpha:
                    break
            return tree[idx]

    damage = alpha_beta_pruning(0, -math.inf, math.inf, branch, depth, True)
    print("Left life (HP) of the defender after maximum damage caused by the attacker", init_hp - damage)
    print("After Alpha-Beta Pruning Leaf Node Comparisons", node_visited)


node_visited = 0 
std_id = (input("Enter your student id: "))
min_v = int(input("Minimum value for the range of negative HP: "))
max_v = int(input("Maximum value for the range of negative HP: "))
ABP(std_id, min_v, max_v)