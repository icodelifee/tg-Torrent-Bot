const axios = require("axios");
const config = require("../config");

const search = async (query, sort) => {
  const queryId = Math.random().toString(36).substring(7);
  const now = new Date();
  const Epoch = Math.round(now.getTime() / 1000);
  return await axios
    .get(config.apiBaseUrl + `${query}/${queryId}/0/SEED/NONE/1?_=${Epoch}`)
    .then(function ({ data }) {
      return data;
    })
    .catch(function (error) {
      console.log("Error " + error.message);
    });
};
module.exports = search;
