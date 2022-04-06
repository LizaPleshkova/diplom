<template>
  <div class="side-bar navbar-nav mr-auto">
    <div class="card border-dark mb-2">
      <div class="card-header border-dark bg-transparent text-dark text-center">
        Кинотеатры
      </div>
      <div class="card-body text-dark">
        <div class="form-check" v-for="cinema in f_cinemas" :key="cinema.id">
          <input
            class="form-check-input"
            type="checkbox"
            :id="cinema.id"
            :value="cinema.name"
            v-model="selectedCinema"
          />
          <label class="form-check-label" :for="cinema.id">
            {{ cinema.name }}</label
          >
        </div>
      </div>
    </div>

    <span>You have chosen: {{ selectedCinema }}</span>

    <div class="card border-dark mb-2">
      <div class="card-header border-dark bg-transparent text-dark text-center">
        Жанры
      </div>
      <div class="card-body text-dark">
        <div class="form-check" v-for="genre in f_genres" :key="genre.id">
          <input
            class="form-check-input"
            type="checkbox"
            :id="genre.id"
            :value="genre.name"
            v-model="selectedGenres"
          />
          <label class="form-check-label" :for="genre.id">
            {{ genre.name }}</label
          >
        </div>
      </div>
    </div>

    <div class="card border-dark mb-2">
      <div class="card-header border-dark bg-transparent text-dark text-center">
        Даты
      </div>
      <div class="card-body text-dark">
        <div class="form-check" v-for="date in f_dates" :key="date.id">
          <input
            class="form-check-input"
            type="checkbox"
            :id="date.id"
            :value="date"
            v-model="selectedDates"
          />
          <label class="form-check-label" for="{{date.id}}">{{ date }}</label>
        </div>
      </div>
    </div>

    <div class="d-grid gap-2 col-6 mx-auto">
      <button
        type="submit"
        value="submit"
        v-on:click="getFilterMovies"
        class="btn btn-outline-dark btn-sm"
      >
        найти
      </button>
    </div>
  </div>
</template>

<script>
import FilterService from "@/services/FilterService.js";
import { mapGetters } from "vuex";


export default {
  name: "Filters",

  data() {
    return {
      f_cinemas: [],
      f_genres: [],
      f_dates: [],

      selectedCinema: [],
      selectedGenres: [],
      selectedDates: [],
    };
  },
  computed: mapGetters(["allMovies"]),
  methods: {
    getFilterMovies: async function () {
      var filters = {
        selectedCinema: this.selectedCinema,
        selectedGenres: this.selectedGenres,
        selectedDates: this.selectedDates,
      };
      console.log("filters", filters);
      this.$store.dispatch("getFilterMovies", filters);
    },
  },

  created() {
    this.$store.dispatch("getFilterMovies");
    FilterService.getFilters().then((filters) => {
      this.f_cinemas = filters["cinemas"];
      this.f_dates = filters["dates"];
      this.f_genres = filters["genres"];
    });
  },
};
</script>
