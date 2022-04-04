import HTTP from "../http-common";

const CinemaService = {
  getCinemas() {
    return HTTP.get("/cinema/").then((response) => {
      return response.data;
    });
  },
  getCinema(pk) {
    return HTTP.get(`/cinema/${pk}`).then((response) => response.data);
  },
};
export default CinemaService;
