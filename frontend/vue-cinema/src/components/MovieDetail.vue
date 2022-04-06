<template>
  <div class="card">
 
    <div class="left-ads-display col-lg-9">
        <div class="row">
            <div class="site-section">
                <div class="container-fluid">
                    <div class="row">
                        <div class="col-md-5 mr-auto">
                            <div class="border text-center">
                                <img v-bind:src="currentMovie.image" alt="Image" class="img-fluid p-5">
                            </div>
                        </div>
                    
                        <div class="col-md-6">
                            <h2 class="text-black">{{ currentMovie.name }}</h2><br>
                            <p>{{ currentMovie.description }}</p>
                            <hr/>

                            <h4 class="text-black">Год:</h4>
                            <p>{{ currentMovie.release_date }}</p>
                            <h4 class="text-black">Страна:</h4>
                            <p></p>
                            <h4 class="text-black">Жанры:</h4>
                            <p></p>
                            <h4 class="text-black">Студия:</h4>
                            <p></p>
                            <h4 class="text-black">Возрастная категория:</h4>
                            <p>{{ currentMovie.category }}+</p>
                            <h4 class="text-black">Длительность:</h4>
                            <p>{{ currentMovie.duration }}</p>
                        </div>
                    </div>
                </div>
                <hr/>

            </div>
        </div>
    </div>
    </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex' 


export default {
  name: "movie-detail",
  computed: mapGetters(["currentMovie"]),
  methods: mapActions(["getMovie"]),
  mounted() {
      console.log('from MD', this.$router.params.movieId);
    this.getMovie(this.$route.params.movieId);
  },
  created() {
      console.log('from MD', this.$router.params.movieId);
    this.getMovie(this.$route.params.movieId);
  }
};
</script>
