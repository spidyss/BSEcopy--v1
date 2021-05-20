<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
html {
  height: 100%;
}

body {
  display: flex;
  flex-direction: column;
  min-height: 100%;
  font-family: 'Poppins', sans-serif;
  background-color: #f4f6fe;
}

.text-bold {
  font-weight: bolder;
}

.text-grey {
  color: grey;
}

.font-56 {
  font-size: 56px;
}

.font-24 {
  font-size: 56px;
}

/*Custom Scrollbar*/

::-webkit-scrollbar {
  width: 5px;
}

::-webkit-scrollbar-thumb {
  background: lightgrey;
}

::-webkit-scrollbar-thumb:hover {
  background: grey;
}

/*End Custom Scrollbar*/
</style>
