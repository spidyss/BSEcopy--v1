<template>
  <div class="mx-auto">
    <form @submit="searchScrips">
      <div class="input-group input-group-lg">
        <input v-model="query" v-on:keyup="keymonitor" type="text" class="form-control border-0 rounded" placeholder="Search by Name" aria-label="Search" id="searchBar">
        <div class="input-group-append">
          <button id="searchButton" type="submit" class="btn btn-link rounded"><i class="fa fa-search"></i></button>
        </div>
      </div>
    </form>
    <div class="border-0 rounded">
      <div class="pb-1">
        <div :key="m.name" v-for="m in match" id="autoComplete">
          <li @click="select(m.name)" :class="m.selected ? 'selected' : 'un-selected'">{{ m.name }}</li>
        </div>
      </div>
    </div>
  </div>  
</template>

<script>
import axios from 'axios';

export default {
  name: 'SearchBar',
  data() {
    return {
      'query': '',
      'names': [],
      'match': [],
      'cursor': -1
    }
  },
  mounted() {
    this.fetchKeys();
  },
  methods: {
    fetchKeys() {
      axios.get(process.env.API_URL + '/api/keys/').then(response => {
        this.names = response.data;
      });
    },
    searchScrips(e) {
      e.preventDefault();
      this.query = this.query.trim().toUpperCase();
      this.$router.push({path:'/data/',query:{name:this.query}});
    },
    keymonitor(e) {
      if(e.key == 'ArrowDown') {
        this.arrowDownListener();
      }
      else if(e.key == 'ArrowUp') {
        this.arrowUpListener();
      }
      else {
        this.match = [];
        if(this.query != '') {
          this.match = this.names.filter((name) => {
            return name.name.toLocaleUpperCase().startsWith(this.query.toLocaleUpperCase());
          });
          if(this.match.length >= 5) {
            this.match = this.match.slice(0, 6);
          }
        }
      }
    },
    select(name) {
      this.query = name;
    },
    arrowDownListener() {
      this.cursor += 1;
      if(this.cursor > 0) {
        this.match[this.cursor - 1].selected = false;

        if(this.cursor > this.match.length - 1) {
          this.cursor = 0;
        }
      }

      this.match[this.cursor].selected = true;
      this.query = this.match[this.cursor].name;
    },
    arrowUpListener() {
      this.cursor -= 1;
      if(this.cursor != -2) {
        this.match[this.cursor + 1].selected = false;
        if(this.cursor < 0) {
          this.cursor = this.match.length - 1;
        }
      }
      else {
        this.cursor = this.match.length - 1;
      }		

      this.match[this.cursor].selected = true;
      this.query = this.match[this.cursor].name;
    }        
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.form-control:focus, .btn-link:focus {
  box-shadow: none;
}

.form-control::placeholder {
  font-size: 20px;
  color: lightgrey;
}

.fa-search {
  color: lightgrey;
}

.fa-search:hover {
  color: grey;
}

#searchButton {
  background-color: white;
}

#autoComplete {
  background-color: white;
}

li {
  list-style: none;
  font-size: 20px;
  padding: 5px 5px 5px 16px;
  cursor: pointer;
}

li:hover {
  background-color: #ebeaf3;
  cursor: pointer;
}

.selected {
  background-color: #ebeaf3;
}
</style>