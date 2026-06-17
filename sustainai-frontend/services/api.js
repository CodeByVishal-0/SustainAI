console.log(
  "API BASE URL:",
  "https://sustainai-backend.onrender.com/api"
);

import axios from "axios";

const API = axios.create({
  baseURL: "https://sustainai-backend.onrender.com/api",
});

export default API;