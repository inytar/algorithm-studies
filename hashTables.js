var HashTable = function(capacity, bucketCapacity){
    this.bucketCapacity = bucketCapacity;
    this.init = function(capacity){
        this.table = [];
        for (var i = 0; i < capacity; i++) {
            this.table.push({});
        };
    };
    this.hashFunction = function(key){
        if (typeof key == "string") {
            var key = hashString(key);
        };
        return key % this.table.length;
    };
    this.store = function(key, value){
        var hash = this.hashFunction(key);
        var bucket = this.table[hash];
        bucket[key] = value;
        if (Object.keys(bucket).length > this.bucketCapacity) {
            console.log(Object.keys(bucket).length + " " + this.bucketCapacity);
            this.redistribute();
        };
    };

    this.redistribute = function() {
        console.log(this.table.length * 2 + 1);
        var rehashReference = this.table;
        this.init(this.table.length * 2 + 1);
        for (var i = 0; i < rehashReference.length; i++) {
            var keysInBucket = Object.keys(rehashReference[i])
            for (var j = 0; j < keysInBucket.length; j++) {
                var key = keysInBucket[j]
                this.store(key, rehashReference[i][key]);
            };
        };
    };

    this.find = function(key){
        return this.table[this.hashFunction(key)][key];
    };

    this.init(capacity);
};

function hashString(string) {
    var sum = 0;
    for (var i=0; i < string.length; i+=4) {
        var mult = 1;
        for (var j=0; j < 4; j++) {
            var index = i + j;
            if (index < string.length) {
                sum += string.charCodeAt(index) * mult;
                mult *= 256;
            } else {
                break;
            };
        };
    };
    var mult = 1;
    for (var i=0; i < string.length; i++) {
        sum += string.charCodeAt(i) * mult;
        mult *= 256;
    };
    return sum;
};

var hashTable = new HashTable(53, 10);
var words = ["go", "stop", "whatever"];
function generateRandomString(){
    var string = "";
    var possibleCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for (var i=0; i < 12; i++) {
        string += possibleCharacters.charAt(Math.floor(Math.random() * possibleCharacters.length));
    };
    return string;
};

for (var n = 0; n < 1000; n++) {
    var key = generateRandomString();
    hashTable.store(key, key);
};

// for (var n = 0; n < 10; n++){
//     console.log(hashTable.find(Math.floor(Math.random() * 1000)));
// }


console.log(hashTable.table);
