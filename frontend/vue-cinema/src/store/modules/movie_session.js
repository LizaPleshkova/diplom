// import CinemaService from "./services/DataService";
import MovieSessionService from "../../services/MovieSessionService.js";
// import axios from 'axios';

const movieSessionModule = {
  actions: {
    async getSeats(context, pk) {
      MovieSessionService.getSeats(pk).then((data) => {

        var ids_booked_seats = Object.keys(data.booked_seats).map(function (
          key
        ) {
          return data.booked_seats[key];
        });

        for (var row in data.seat_layout) {
          var seats = data.seat_layout[row];

          for (var k_seat in seats) {
            if (ids_booked_seats.indexOf(seats[k_seat].id) != -1) {
              seats[k_seat]["isBooked"] = true;
            } else {
              seats[k_seat]["isBooked"] = false;
            }
          }
        }

        context.commit("set_seats", data.seat_layout);
        context.commit("set_booked_seats", data.booked_seats);
        context.commit("set_movie_session", data.movie_session);
      });
    },
    async BookedSeats(context,selectedSeats) {
      MovieSessionService.bookSeats(selectedSeats, this.getters.movieSession.id).then((data) => {
        context.commit('set_new_booked', data)
      });
    },
  },
  mutations: {
    set_seats(state, seats) {
      state.seats = seats;
    },
    set_booked_seats(state, booked_seats) {
      state.booked_seats = booked_seats;
    },
    set_movie_session(state, m_session) {
      state.movie_session = m_session;
    },
    set_new_booked(state, newBookSeats) {
      state.newBookSeats = newBookSeats;
    },
  },
  state: {
    seats: [],
    booked_seats: [],
    movie_session: null,
    newBookSeats:[],
  },
  getters: {
    allSeats(state) {
      return state.seats;
    },
    movieSession(state) {
      return state.movie_session;
    },
    bookedSeats(state) {
      return state.booked_seats;
    },
    newBookSeats(state) {
      return state.newBookSeats;
    },
  },
};

export default movieSessionModule;
