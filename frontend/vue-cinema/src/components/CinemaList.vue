<template>
  <div class="container-fluid">
      <h1>from cinema list</h1>
      <Cinema
        v-for="cinema in allCinemas"
        v-bind:key="cinema.id"
        :cinema="cinema"
      />
  </div>
</template>

<script>
import Cinema from "./Cinema.vue";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "CinemaList",
  components: {
    Cinema,
  },
  computed: mapGetters(["allCinemas"]),
  methods: mapActions(["getCinemas"]),
  mounted() {
    this.getCinemas();
    console.log(this.allCinemas);
  },
};
</script>
