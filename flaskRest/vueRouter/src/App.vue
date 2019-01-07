<template>
  <div id="app">
    <ul id="nav" class="nav">
      <li>
        <router-link to="/home" class="nav-link active">Home</router-link>
      </li>
      <li>
        <router-link to="/users" class="nav-link">Users</router-link>
      </li>
      <li>
        <router-link to="/about" class="nav-link">About</router-link>
      </li>
    </ul>
    <hr>
    <router-view />
  </div>
</template>
<style>
  #app {
    /* font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 10px; */
    width: 80%;
    margin: 0 auto;
  }

  #nav {
    font-size: 2em;
  }
</style>