
<template>
    <div id='#app'>
    <div class="nav">
      <div>
        <router-link to="/" > Movies </router-link>
        <router-link to="/cinema"> Cinemas </router-link>
      </div>
  <router-view/>
          </div>
          </div>
           
</template>

<script>
// import MovieList from './components/MovieList'
// import MovieList from './MovieList'

export default {
  name: 'App',
  data(){
    return{
      movies:[],
      cinemas:[]
    }
  },
  // components:{
  //   MovieList,
  // }
}
</script>