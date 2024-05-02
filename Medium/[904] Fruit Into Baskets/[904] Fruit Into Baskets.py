"""
Accepted
904 [Medium]
Runtime: 658 ms, faster than 73.91% of Python3 online submissions for Fruit Into Baskets.
Memory Usage: 24.27 MB, less than 23.56% of Python3 online submissions for Fruit Into Baskets.
"""
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        count = 2
        res = 0
        hashMap = defaultdict(int)
        for right in range(len(fruits)):
            if hashMap[fruits[right]] == 0:
                count -= 1
            hashMap[fruits[right]] += 1
            while count == -1 and left < right:
                hashMap[fruits[left]] -= 1
                if hashMap[fruits[left]] == 0:
                    count += 1
                left += 1
            res = max(res, right - left + 1)
        return res
    


"""
Previous attempts in Java
//904 [Medium]Fruit Into Baskets
class Solution {
    int trees[]=new int[2],max=1,max1=0,fir_place=0,i;
    public int totalFruit(int[] fruits) {
        boolean b=false;
        trees[0]=fruits[0];
        trees[1]=-1;
        for(i=0;i<fruits.length;i++) {
            if(i==fruits.length-1) {
                b=true;
                break;
            }
            if(fruits[i]!=trees[0]) {
                trees[1]=fruits[i];
                fir_place=i;
                break;
            }
        }
        while(b!=true) {
            for(i=fir_place;i<fruits.length;i++) {
                if(max<max1)
                    max=max1;
                max1=0;
                if(fruits[i]==trees[0] || fruits[i]==trees[1])
                    max1++;
                if(fruits[i]!=trees[0] || fruits[i]!=trees[1]) {
                    trees[0]=trees[1];
                    trees[1]=fruits[i];
                    fir_place=i;
                }
                if(i==fruits.length-1)
                    b=true;
            }
        }
        return max;
    }
}


//904 [Medium]Fruit Into Baskets
class Solution {
    int trees[]=new int[2],max=1,max1=0,fir_place=0,i;
    public int totalFruit(int[] fruits) {
        boolean b=false;
        trees[0]=fruits[0];
        trees[1]=-1;
        for(i=0;i<fruits.length;i++) {
            if(i==fruits.length-1) {
                max=fruits.length;
                b=true;
                break;
            }
            if(fruits[i]!=trees[0]) {
                trees[1]=fruits[i];
                fir_place=i;
                break;
            }
        }
        while(b!=true) {
            System.out.println("b is false");
            for(i=fir_place;i<fruits.length;i++) {
                if(max<max1)
                    max=max1;
                max1=0;
                if(fruits[i]==trees[0] || fruits[i]==trees[1])
                    max1++;
                if(fruits[i]!=trees[0] || fruits[i]!=trees[1]) {
                    trees[0]=trees[1];
                    trees[1]=fruits[i];
                    fir_place=i;
                }
                if(i==fruits.length-1)
                    b=true;
            }
        }
        return max;
    }
}


//904 [Medium]Fruit Into Baskets
class Solution {
    int trees[]=new int[2],max=1,max1=0,fir_place=0,i;
    public int totalFruit(int[] fruits) {
        boolean b=false;
        trees[0]=fruits[0];
        trees[1]=-1;
        for(i=0;i<fruits.length;i++) {
            if(i==fruits.length-1) {
                max=fruits.length;
                b=true;
                break;
            }
            if(fruits[i]!=trees[0]) {
                trees[1]=fruits[i];
                fir_place=i;
                break;
            }
        }
        while(b!=true) {
            System.out.println("b is false");
            System.out.println(fir_place);
            for(i=fir_place;i<fruits.length;i++) {
                if(max<max1)
                    max=max1;
                max1=0;
                if(fruits[i]==trees[0] || fruits[i]==trees[1])
                    max1++;
                if(fruits[i]!=trees[0] || fruits[i]!=trees[1]) {
                    trees[0]=trees[1];
                    trees[1]=fruits[i];
                    fir_place=i;
                }
                if(i==fruits.length-1)
                    b=true;
            }
        }
        return max;
    }
}


class Solution {
    public int totalFruit(int[] fruits) {
        int max=1,trees[]=new int[2],i;
        trees[0]=fruits[0];
        trees[1]=-1;
        if(fruits.length==1)
            return 1;
        for(i=0;i<fruits.length;i++) {
            if(trees[0]!=fruits[i] && trees[1]!=fruits[i])
            if(fruits[i]!=trees[0]) {
                trees[1]=fruits[i];
                continue;
            }
            if(trees[0]!=fruits)
        }
    }
}
"""