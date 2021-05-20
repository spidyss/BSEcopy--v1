<template>
    <div>
        <NavBar v-if="data.length != 0 && !loading"></NavBar>
        <Spinner v-if="loading"></Spinner>
        <div v-else class="container">
            <div v-if="data.length != 0">
                <div class="row mt-5 pt-5 pl-4">
                    <p v-if="name.length != 0">Search results for "{{ name }}"</p>
                    <p v-else>Showing all the results</p>
                </div>
                <div class="row mb-4 pr-4 justify-content-end">
                    <button @click="exportCSV" type="botton" class="btn btn-primary btn-lg rounded export-button">Export CSV</button>
                </div>
                <div class="row my-5 px-4">
                    <div class="table-responsive">
                        <table class="table table-hover table-borderless">
                            <thead>
                                <tr>
                                    <th scope="col" class="align-middle">CODE</th>
                                    <th scope="col" class="align-middle">NAME</th>
                                    <th scope="col" class="align-middle">OPEN</th>
                                    <th scope="col" class="align-middle">HIGH</th>
                                    <th scope="col" class="align-middle">LOW</th>
                                    <th scope="col" class="align-middle">CLOSE</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr :key="d.code" v-for="d in data">
                                    <td>{{ d.code }}</td>
                                    <td>{{ d.name }}</td>
                                    <td>{{ d.open }}</td>
                                    <td>{{ d.high }}</td>
                                    <td>{{ d.low }}</td>
                                    <td>{{ d.close }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            <div v-else>
                <NoMatch :name="name"></NoMatch>
            </div>            
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import NavBar from '../components/NavBar';
import Spinner from '../components/Spinner';
import NoMatch from '../components/NoMatch';

export default {
  name: 'Data',
  components: {
    NavBar,
    Spinner,
    NoMatch
  },
  data() {  
    return {
      'name': this.$route.query.name,
      'loading': true,
      'headers': {},
      'data': []
    }
  },
  created() {
      this.headers = {
        'code': 'SC_CODE',
        'name': 'SC_NAME',
        'group': 'SC_GROUP',
        'type': 'SC_TYPE',
        'open': 'OPEN',
        'high': 'HIGH',
        'low': 'LOW',
        'close': 'CLOSE',
        'last': 'LAST',
        'prevclose': 'PREVCLOSE',
        'no_trades': 'NO_TRADES',
        'no_of_shares': 'NO_OF_SHRS',
        'net_turnover': 'NET_TURNOV',
        'tdcloindi': 'TDCLOINDI'
      };
      this.fetchData();
  },
  methods: {
    fetchData() {
        axios.get(process.env.API_URL + '/api/data/?q=' + this.name).then(response => {
            if(response.data != null) {
                this.data = response.data;
            }
            else {
                this.data = [];
            }
            this.loading = false;
        });
    },
    exportCSV() {
        let fileTitle = 'data';
        this.exportCSVFile(this.headers, this.data, fileTitle);
        this.data.shift();
    },
    convertToCSV(objArray) {
        var array = typeof objArray != 'object' ? JSON.parse(objArray) : objArray;
        var str = '';

        for (var i = 0; i < array.length; i++) {
            var line = '';
            for (var index in array[i]) {
                if (line != '') line += ','

                line += array[i][index];
            }

            str += line + '\r\n';
        }

        return str;
    },
    exportCSVFile(headers, items, fileTitle) {
        if (headers) {
            items.unshift(headers);
        }
        var jsonObject = JSON.stringify(items);
        var csv = this.convertToCSV(jsonObject);
        var exportedFilenmae = fileTitle + '.csv' || 'export.csv';
        var blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });

        if (navigator.msSaveBlob) {
            navigator.msSaveBlob(blob, exportedFilenmae);
        }
        else {
            var link = document.createElement("a");
            if (link.download !== undefined) {
                var url = URL.createObjectURL(blob);
                link.setAttribute("href", url);
                link.setAttribute("download", exportedFilenmae);
                link.style.visibility = 'hidden';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            }
        }
    }
  }
}
</script>

<style scoped>
.btn-primary {
    background-color: #5b63fe;
}
</style>
