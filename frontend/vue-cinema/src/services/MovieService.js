import HTTP from "../http-common";
import axios from "axios";

const MovieService = {
  getMovies() {
    // return axios.get(`http://localhost:8000/api/movie/`).then((response) => {
    return axios.get(`http://localhost:8000/api/movie/current_movies/`).then((response) => {
      return response.data;
    });
  },
  getMoviesSoon() {
    return HTTP.get("/movie/soon/").then((response) => {
      return response.data;
    });
  },
  getMoviesLatest() {
    return HTTP.get("/movie/latest/").then((response) => {
      return response.data;
    });
  },
  getMovie(pk) {
    return HTTP.get(`/movie/${pk}/`).then((response) => response.data);
    // return  axios.get(`http://localhost:8000/api/movie/${pk}/`).then((response) => response.data);
  },
  getFilterMovies(filters) {
    var cinemas = get_list_filter(filters, "selectedCinema");
    var genres = get_list_filter(filters, "selectedGenres");
    var dates = get_list_filter(filters, "selectedDates");
    var api_url = set_filter_url(cinemas, genres, dates);
    return axios.get(api_url).then((response) => response.data);
  },
};

function get_list_filter(filters, key) {
  var arr = [];
  var selectedCinema = filters[key];

  for (var arr_key in selectedCinema) {
    arr.push(selectedCinema[arr_key]);
  }
  return arr;
}

function set_filter_url(cinemas, genres, dates) {
  var api_url = new URL("http://localhost:8000/api/movie/");
  if (Object.keys(cinemas).length != 0) {
    api_url.searchParams.append("cinema", cinemas.join(","));
  }
  if (Object.keys(genres).length != 0) {
    api_url.searchParams.append("genre", genres);
  }
  if (Object.keys(dates).length != 0) {
    api_url.searchParams.append("date", dates);
  }
  return api_url;
}

export default MovieService;
