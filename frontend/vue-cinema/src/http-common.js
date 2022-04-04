import axios from "axios";

const HTTP = axios.create({
  baseURL: `http://localhost:8000/api/`,
  headers: {
    "Content-type": "application/json",
  },
});
export const HTTP_USER = axios.create({
  baseURL: `http://localhost:8000/client/`,
  headers: {
    "Content-type": "application/json",
  },
});

export default HTTP;
