import axios from "axios";

const FilterService = {
  getFilters() {
    return axios.get(`http://localhost:8000/api/filters/`).then((response) => {
      return response.data;
    });
  },
};
export default FilterService;
