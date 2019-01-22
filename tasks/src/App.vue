<template>
  <div id="app">
    <h1>Data visualization</h1>
    <div id="nav">
        <router-link :to="{ name: 'patients' }" style="padding-right: 15px">Assignment 1</router-link>
        <router-link :to="{ name: 'charts' }" style="padding-right: 15px">Assignment 2</router-link>
        <router-link :to="{ name: 'netcdf' }" style="padding-right: 15px">Assignment 3-4</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
