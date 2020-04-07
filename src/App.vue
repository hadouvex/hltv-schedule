<template>
  <div id="app">
    <div v-for="match in matches" :key="match.id">
      <div>#{{ match.index }} <b>|</b> {{ match.date_cet }} CET <b>|</b> {{ match.date_msc }} MSC <b>|</b> <b>{{ match.team_a }}</b> vs <b>{{ match.team_b }}</b>
       <b>|</b> {{ match.event }} <b>|</b> {{ match.match_type }}</div><br>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      matches: null
    }
  },
  methods: {
    GetMatches: function() {
      var vm = this
      axios.get(process.env.API_URL + "/api/matches")
      .then(response => {
        vm.matches = response.data;
        JSON.stringify(vm.matches);
      })
    }
  },
  created: function() {
    this.GetMatches();
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  color: #2c3e50;
  margin-top: 10px;
}
</style>
