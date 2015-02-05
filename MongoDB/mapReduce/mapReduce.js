map1 = function() {
    emit(this.reputation_color, 1)
}

// reduce1 = function(key, vals) {
//     for(var i=0, sum=0; i < vals.lenght ; i++) {
//         sum += vals[i];
//     }
//     return sum;
// }

reduce1 = function(key, vals) {
    return key, vals
} 

var res1 = db.collection.mapreduce(map1, reduce1)
// creates a collection in database
db[res1.results].find()
