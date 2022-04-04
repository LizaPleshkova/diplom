import HTTP from "../http-common";

const MovieService = {
  getMovies() {
    return HTTP.get("/movie/").then((response) => {
      return response.data;
    });
  },
  getMovie(pk) {
    return HTTP.get(`/movie/${pk}`).then((response) => response.data);
  },
};
export default MovieService;
