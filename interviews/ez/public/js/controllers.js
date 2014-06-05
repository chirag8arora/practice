var controllers = angular.module('myApp.controllers', []);
controllers.controller('Question1', function($scope, $http) {
    // d3
    var margin = {
            top: 20,
            right: 20,
            bottom: 30,
            left: 40
        },
        width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    var svg = d3.select(".q1").append('svg')
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


    $scope.render = function(dataset) {
        // remove previous items before render
        svg.selectAll('*').remove();

        // edge case
        if (!dataset) return;

        // setup x, y
        var x = d3.scale.ordinal()
            .rangeRoundBands([0, width], .1)
            .domain(dataset.map(function(d, i) {
                if (i == 26) return '?';
                return String.fromCharCode(65 + i);
            }));

        var y = d3.scale.linear()
            .range([height, 0])
            .domain([0, d3.max(dataset, function(d) {
                return d;
            }) + 2]);

        // setup xAxis and yAxis
        var xAxis = d3.svg.axis()
            .scale(x)
            .orient("bottom");
        var yAxis = d3.svg.axis()
            .scale(y)
            .orient("left")

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

        //create the rectangles
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
            .attr('fill', 'orange')
            .attr("width", x.rangeBand())
            .attr("height", function(d) {
                return height - y(d);
            });
    }
    $scope.search = function(userSearchKey) {
        var url = 'https://api.angel.co/1/search?query=' + userSearchKey + '&type=User&callback=JSON_CALLBACK';
        $http({
            method: 'JSONP',
            url: url
        }).success(function(data, status, header, config) {
            var dataset = Array.apply(null, new Array(27)).map(Number.prototype.valueOf, 0);
            data.slice(0, Math.min(data.length, 5)).forEach(function(user) {
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
            $scope.render(dataset);
        });
    };
}).controller('Question2', function($scope, $http) {
    $scope.get_missing_letters = function(sentence) {
        sentence = sentence||'';
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
}).controller('Question3', function($scope, $http) {
    $scope.result = [];
    $scope.errs = [];
    $scope.go = function(step, initial) {
        // clear previous errs and result;
        $scope.errs = [];
        $scope.result = [];

        // set default parameters
        step = step || 1;
        initial = initial || 'R....';

        // validate the input
        var reg = /^\d+$/;
        if (!reg.test(step)) {
            $scope.errs.push('The step must be integer');
        }
        reg = /^[.LR]+$/;
        if (!reg.test(initial)) {
            $scope.errs.push('The initial state can only have ".", "L", "R"');
        }
        if ($scope.errs.length > 0) return;

        // initial state for counters of left and right
        // for example ..LRR... => state = {left: [2], right:[3,4]}
        var state = {
            left: [],
            right: []
        }
        for (var i = 0; i < initial.length; i++) {
            if (initial.charAt(i) == 'L') {
                state.left.push(i); // add the index to state.left
            } else if (initial.charAt(i) == 'R') {
                state.right.push(i); // add the index to state.left
            }
        }

        // start moving particles
        while (true) {
            // initial a result buffer and empty_flag
            var current_state = '';
            var empty_flag = true;
            // dump the state to a result string, '..LR..' -> '..XX..'
            for (var i = 0; i < initial.length; i++) {
                if (state.left.indexOf(i) >= 0 || state.right.indexOf(i) >= 0) {
                    // position i is in either left or right array
                    // the graph is not empty
                    // and assign a X to this position
                    empty_flag = false;
                    current_state += 'X';
                } else {
                    // position i is neither in left nor in right
                    // assign a . to this position
                    current_state += '.';
                }
            }
            // put this current state to the result array
            $scope.result.push(current_state);
            // if empty_flag is true, means no particle in the graph, should break
            if (empty_flag) break;


            // move the particles for next time inteval
            state.left.forEach(function(l, i) {
                state.left[i] = l - parseInt(step);
                // out of boundry, set to null
                if (state.left[i] < 0) state.left[i] = null;
            });
            state.right.forEach(function(r, i) {
                state.right[i] = parseInt(r) + parseInt(step);
                // out of boundry, set to null
                if (state.right[i] >= initial.length) state.right[i] = null;
            });
        }
    };
}).controller('navCtrl', ['$scope', '$location',
    function($scope, $location) {
        $scope.navClass = function(page) {
            var currentRoute = $location.path().substring(1) || 'question1';
            return page === currentRoute ? 'active' : '';
        };
    }
]);;
