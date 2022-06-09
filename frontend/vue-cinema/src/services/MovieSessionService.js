import HTTP from "../http-common";


const MovieSessionService = {
  getSeats(pk) {
    return HTTP.get(`/movie-session/${pk}/seats/`).then((response) => {
      return response.data;
    });

  },
  bookSeats(selectedSeats, pk){
    // обновлять ids_booked-seats?
    return HTTP.post(
      `/booking/${pk}//movie-session/booking-seats/`, selectedSeats
    ).then((response) => {
      return response.data;
    }); 
  }
};

export default MovieSessionService;
