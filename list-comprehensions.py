# Reference: List of practice problems from the repo of doughsay - https://gist.github.com/doughsay/cb50d9e4d344230ebc166255a202f81d

def identity(nums):
    copied_nums = nums[:]
    return copied_nums

def doubled(nums):
    x =[each*2 for each in nums]
    return x

def squared(nums):
    x = [each**2 for each in nums]
    return x
    
def evens(nums):
    x = [ each for each in nums if each%2==0]
    return x

def odds(nums):
    x = [ each for each in nums if each%2!=0]
    return x

def positives(nums):
    x =[ each for each in nums if each>=0]
    return x
def selective_stringify_nums(nums):
    x = [str(each) for each in nums if each%5==0]
    return x

def words_not_the(sentence):
    lengths =[len(eachs) for eachs in sentence.split(" ") if eachs not in ('the')]
    return lengths

def vowels(word):
    x = ([vowels for vowels in vow if vowels in ('a','e','i','o','u')])
    return x

def vowels_set(word):
    x = (set([vowels for vowels in vow if vowels in ('a','e','i','o','u')]))
    return x
    
def disemvowel(sentence):
    y = [item for item in sentence if item not in ('a','e','i','o','u') ]
    return ''.join(y)
 
def wiggle_numbers(nums):
    x = [each*2 if each%2==0 else (0-each) for each in nums ]
    return x

def encrypt_lol(sentence):
    x=[chr(ord(each)+1) if ord(each) in range(ord('a'),ord('y')) else each for each in sentence]
    return ''.join(x)

if __name__=="__main__":
    nums1=[1,2,3,4,5]
    print(identity(nums1))
    nums2=[-2, 2, -10, 10]
    print(doubled(nums1))
    print(doubled(nums2))
    print(squared(nums1))
    print(squared(nums2))
    nums3=[1,3,5]
    nums4=[-2, -4, -7]
    print(evens(nums4))
    print(evens(nums3))
    nums5=[2, 4, 6]
    print(odds(nums1))
    print(odds(nums5))
    print(odds(nums4))
    nums6=[-2, -1, 0, 1, 2]
    print(positives(nums6))
    nums7=[25, 91, 22, -7, -20]
    print(selective_stringify_nums(nums7))
    sent='the quick brown fox jumps over the lazy dog'
    print(words_not_the(sent))
    vow='mathematics'
    print(vowels(vow))
    print(vowels_set(vow))
    sentence='the quick brown fox jumps over the lazy dog'
    print(disemvowel(sentence))
    nums8=[72, 26, 79, 70, 20, 68, 43, -71, 71, -2]
    print(wiggle_numbers(nums8))
    sent2='the quick brown fox jumps over the lazy dog'
    print(encrypt_lol(sent2))
    
