import HTTP from "../http-common";
import axios from "axios";



const MovieService = {
  getMovies() {
    // console.log(this.$state, this.$state.getters)
    // console.log(this.$store.state.authModule.user.accessToken)
    return HTTP.get("/movie/").then((response) => {
      return response.data;
    });
  },

  getMovie(pk) {
    console.log('from MS')
    return HTTP.get(
      `/movie/${pk}/`
    //  { headers: {
    //     Authorization: 'Bearer ' + token //the token is a variable which holds the token
    //   }}
      ).then((response) => response.data);
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
  console.log(typeof(cinemas), cinemas.join(','))
  if (Object.keys(cinemas).length != 0) {
    api_url.searchParams.append("cinema", cinemas.join(','));
  }
 if (Object.keys(genres).length != 0) {
    api_url.searchParams.append("genre", genres);
  }
  if (Object.keys(dates).length != 0) {
    api_url.searchParams.append("date", dates);
  }
  console.log(api_url);
  return api_url;
}

export default MovieService;
