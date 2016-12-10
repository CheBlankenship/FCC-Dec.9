# FIND THE LONGEST STRING

# function findLongestWord(str) {
#   var result = [];
#   var check = str.split(" ");
#   var word = 0;
#   for(var i=0; i<=check.length-1; i++){
#     var position = check[i];
#     var strlen = position.length;
#     if(strlen > word){
#       word = strlen;
#       result = position;
#     }
#   }
#   return result.length;
# }
# console.log(findLongestWord("The quick brown fox jumped over the lazy dog"));

def findLongestWord(string):
    change = string.split(" ")
    count = 0
    ans = ""

    length = len(change)
    for i in range(length):
        # print change[i]
        positionLength = len(change[i])
        # print positionLength
        if count < positionLength:
            count = positionLength
            ans = change[i]

    print ans






findLongestWord("hi i am longets man!")
