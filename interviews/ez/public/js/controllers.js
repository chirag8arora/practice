var controllers = angular.module('myApp.controllers', []);
controllers.controller('HomeCtrl', function($scope, $http) {
    $scope.search = function(userSearchKey) {
        var url = 'https://api.angel.co/1/search?query=' + userSearchKey + '&type=User&callback=JSON_CALLBACK';
        $http({
            method: 'JSONP',
            url: url
        }).success(function(data, status, header, config) {
            $('.q1 svg').remove();
            var counter = 0;
            var dataset = Array.apply(null, new Array(27)).map(Number.prototype.valueOf, 0);
            data.forEach(function(user) {
                counter++;
                if (counter > 5) return;
                for (var i = 0; i < user.name.length; i++) {
                    var charCode = user.name.charCodeAt(i);
                    if (charCode <= 122 && charCode >= 97) {
                        dataset[charCode - 97] += 1;
                    } else if (charCode <= 90 && charCode >= 65) {
                        dataset[charCode - 65] += 1;
                    } else {
                        dataset[26] += 1;
                    }
                }
            });

            // d3
            var margin = {
                    top: 20,
                    right: 20,
                    bottom: 30,
                    left: 40
                },
                width = 960 - margin.left - margin.right,
                height = 500 - margin.top - margin.bottom;

            var x = d3.scale.ordinal()
                .rangeRoundBands([0, width], .1);

            var y = d3.scale.linear()
                .range([height, 0]);

            var xAxis = d3.svg.axis()
                .scale(x)
                .orient("bottom");

            var yAxis = d3.svg.axis()
                .scale(y)
                .orient("left")

            var svg = d3.select(".q1").append('svg')
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


            x.domain(dataset.map(function(d, i) {
                if (i == 26) return '?';
                return String.fromCharCode(65 + i);
            }));
            y.domain([0, d3.max(dataset, function(d) {
                return d;
            }) + 2]);

            svg.append("g")
                .attr("class", "x axis")
                .attr("transform", "translate(0," + height + ")")
                .call(xAxis);

            svg.append("g")
                .attr("class", "y axis")
                .call(yAxis)
                .append("text")
                .attr("transform", "rotate(-90)")
                .attr("y", 6)
                .attr("dy", ".71em")
                .style("text-anchor", "end")
                .text("Count");

            svg.selectAll(".bar")
                .data(dataset)
                .enter()
                .append("rect")
                .attr("x", function(d, i) {
                    if (i == 26) return x('?');
                    return x(String.fromCharCode(65 + i));
                })
                .attr("y", function(d) {
                    return y(d); //Height minus data value
                })
                .attr("width", x.rangeBand())
                .attr("height", function(d) {
                    return height - y(d);
                });
        });
    };
    $scope.get_missing_letters = function(sentence) {
        var dataset = Array.apply(null, new Array(26)).map(Number.prototype.valueOf, 0);
        for (var i = 0; i < sentence.length; i++) {
            var charCode = sentence.charCodeAt(i);
            if (charCode <= 122 && charCode >= 97) {
                dataset[charCode - 97] += 1;
            } else if (charCode <= 90 && charCode >= 65) {
                dataset[charCode - 65] += 1;
            }
        }
        $scope.missing = ''
        dataset.forEach(function(d, i) {
            if (d == 0) {
                $scope.missing += String.fromCharCode(97 + i);
            }
        });
    };
    $scope.result = [];
    $scope.go = function(step, initial) {
        $scope.result = [];
        state = {
            left: [],
            right: []
        }
        for (var i = 0; i < initial.length; i++) {
            if (initial.charAt(i) == 'L') {
                state.left.push(i);
            } else if (initial.charAt(i) == 'R') {
                state.right.push(i);
            }
        }
        // var counter = 0;
        while (true) {

            var current_state = '';
            var empty_flag = true;
            for (var i = 0; i < initial.length; i++) {
                if (state.left.indexOf(i) >= 0 || state.right.indexOf(i) >= 0) {
                    empty_flag = false;
                    current_state += 'X';
                } else {
                    current_state += '.';
                }
            }
            $scope.result.push(current_state);
            // break;
            if (empty_flag) break;
            // counter += 1;
            // if (counter >= 4) break;
            // move
            state.left.forEach(function(l, i) {
                state.left[i] = l - parseInt(step);
                if (state.left[i] < 0) state.left[i] = null;
            });
            state.right.forEach(function(r, i) {
                state.right[i] = parseInt(r) + parseInt(step);
                if (state.right[i] >= initial.length) state.right[i] = null;
            });
            console.log(state);
        }
    };
});
