// import HTTP from "../http-common";
import axios from 'axios'

const headers = { 
  "Content-type": "application/json",
  'Authorization': "Bearer " + localStorage.getItem('token')
};

const FilterService = {
    getFilters() {
    return axios.get(`http://localhost:8000/api/filters/`, {headers}).then((response) => {
        console.log(response.data);
      return response.data;
    });
  }
};
export default FilterService;
