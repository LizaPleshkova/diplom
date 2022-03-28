<template>
    <div id='#app'>
        <ul><h2>List of cinemas</h2>
        <li v-for="cinema in cinemas" :key = "cinema.id">
        {{ cinema.name }}     {{ cinema.address }}</li>
        </ul>

    </div>
</template>

<script>

export default {
  name: 'App',
  data(){
    return{
      cinemas:[]
    }
  },
  async created(){
    var response = await fetch('http://localhost:8000/api/cinema/');
    this.cinemas = await response.json();console.log(this.cinema);
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
