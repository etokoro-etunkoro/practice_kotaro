import heapq

heap = [2,4,5,22,9,1]   #通常のリスト

heapq.heapify(heap)     #リストがヒープに変換された [1,2,4,5,9,22]

heap[0]                 #最小の要素にアクセス　→　1


heapq.heappop(heap)     #最小の要素を取り出す　→ 2,4,5,9,22

heapq.heappush(heap, 5) #要素の追加　→　[2,4,5,5,9,22]

len(heap)               #ヒープの長さ →　6