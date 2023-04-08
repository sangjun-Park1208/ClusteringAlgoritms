// let tf = require('@tensorflow/tfjs')
// let {LinearRegression, setBackend, KMeans} = require('scikitjs');
// setBackend(tf)

// // Perform a linear regression

// let X = [];
// for(let i=0; i<100; i++){
//     X.push([Math.floor(Math.random()*100) % 100, Math.floor(Math.random()*100) % 100]);
// }
// // let y = [10, 14, 20]

// let kmean = new KMeans({nClusters: 3})
// console.log(kmean.toJSON(X).then((v)=> console.log(v)))

const axios = require("axios");

getTest = async (req, res, next) => {
    try{
        const response = await axios.get("http://localhost:5000");
        console.log(response.data);
        res.status(201).send(response.data);
    } catch(error) {
        console.log(error);
    }
};

module.exports = getTest;