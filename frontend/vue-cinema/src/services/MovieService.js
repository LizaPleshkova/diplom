import HTTP from "../http-common";
import axios from "axios";

const MovieService = {
  getMovies() {
    return HTTP.get("/movie/").then((response) => {
      return response.data;
    });
  },

  getMovie(pk) {
    return HTTP.get(`/movie/${pk}`).then((response) => response.data);
  },

  getFilterMovies(filters) {
    console.log(filters);
    var cinemas = get_list_filter(filters, "selectedCinema");
    var genres = get_list_filter(filters, "selectedGenres");
    var dates = get_list_filter(filters, "selectedDates");

    console.log(cinemas, genres, dates);

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
  if (cinemas != null) {
    for (let key1 in cinemas) {
      console.log(cinemas[key1]);
      api_url.searchParams.append("cinema", cinemas[key1]);
    }
  }
  console.log('after c ', api_url)
  if (genres != null) {
    for (let key1 in genres) {
      console.log(genres[key1]);
      api_url.searchParams.append("genre", genres[key1]);
    }
  }
  console.log('after g', api_url)

  if (dates != null) {
    for (let key1 in dates) {
      console.log(dates[key1]);
      api_url.searchParams.append("date", dates[key1]);
    }
  }
  console.log(api_url);
  return api_url;
}

export default MovieService;
