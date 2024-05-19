def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
     if (sum(gas) < sum(cost)):
          return -1

     current_gaz = 0
     best_start = 0
     for i in range(len(gas)):
          current_gaz += gas[i] - cost[i]
          if current_gaz < 0:
               current_gaz = 0
               best_start = (i + 1) % len(cost)

     return best_start

assert(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) == 3)