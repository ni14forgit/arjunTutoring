var list1 = [1, 2, 3, 4, 5, 5];
var list2 = [1, 2, 4, 6, 5];

var mylist = [1, 2, 3, 4, 5, 5];

var answer = [1, 2, 4, 5];

// give me the numbers [2, 4, 6]
//code here

for (var i = 0; i < mylist.length; i++) {
  if (mylist[i] !== 1 && mylist[i] !== 3 && mylist[i] !== 5) {
    answer.push(mylist[i]);
  }
  //console.log("after evaluating the " + i + "th element which is " + mylist[i]);
  //console.log("this is answer currently " + answer);
}

console.log(answer);

//Problem 2

var arjun = [1, 2, 3, 4, 5];

var myset = new Set([1, "arjun", 3, 4, 5, 6, 6]);
console.log(myset);

//ANSWER WITH SET

var newSet = new Set(list2);

var answer = [];

for (var i = 0; i < list1.length; i++) {
  if (newSet.contains(list1[i])) {
    answer.push(list1[i]);
  }
}

// set.contains()

// HW for Arjun

firstList = [1, 2, 4, 6, 8];
secondtList = [2, 5, 6, 8];
answer = [];

// remember to use set, look in above code to see how it is instantiated
//answer should be [2,6,8]
