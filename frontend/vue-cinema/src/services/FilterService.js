import HTTP from "../http-common";

const FilterService = {
    getFilters() {
    return HTTP.get("/filters/").then((response) => {
        console.log(response.data);
      return response.data;
    });
  }
};
export default FilterService;
