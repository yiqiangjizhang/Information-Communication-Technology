/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

// Wait for the deviceready event before using any of Cordova's device APIs.
// See https://cordova.apache.org/docs/en/latest/cordova/events/events.html#deviceready

var app = {
  // Initialize function
  initialize: function () {
    // Create event
    document.addEventListener(
      "deviceready", // Device must be ready (Cordova environment)
      this.onDeviceReady.bind(this), // Run application
      false
    );
  },

  // Function to print on console
  onDeviceReady: function () {
    console.log("Event Device Ready received");

    document.getElementById("query_temp").addEventListener(
      "click", // Device must be ready (Cordova environment)
      app.onQueryTempButtonClick.bind(app), // Run application
      false
    );

    document.getElementById("query_press").addEventListener(
      "click", // Device must be ready (Cordova environment)
      app.onQueryPressButtonClick.bind(app), // Run application
      false
    );

    document.getElementById("query_hum").addEventListener(
      "click", // Device must be ready (Cordova environment)
      app.onQueryHumButtonClick.bind(app), // Run application
      false
    );

    document.getElementById("query_temp_hum").addEventListener(
      "click", // Device must be ready (Cordova environment)
      app.onQueryTempHumButtonClick.bind(app), // Run application
      false
    );

    document.getElementById("query_temp_press").addEventListener(
      "click", // Device must be ready (Cordova environment)
      app.onQueryTempPressButtonClick.bind(app), // Run application
      false
    );

    document.getElementById("query_magn").addEventListener(
      "click", // Device must be ready (Cordova environment)
      app.onQueryMagnButtonClick.bind(app), // Run application
      false
    );

    document.getElementById("query_acc").addEventListener(
      "click", // Device must be ready (Cordova environment)
      app.onQueryAccButtonClick.bind(app), // Run application
      false
    );

    document.getElementById("query_gyro").addEventListener(
      "click", // Device must be ready (Cordova environment)
      app.onQueryGyroButtonClick.bind(app), // Run application
      false
    );

    document.getElementById("query_IMU").addEventListener(
      "click", // Device must be ready (Cordova environment)
      app.onQueryIMUButtonClick.bind(app), // Run application
      false
    );

    document.getElementById("query_temp").disabled = false;
    document.getElementById("query_press").disabled = false;
    document.getElementById("query_hum").disabled = false;
    document.getElementById("query_temp_hum").disabled = false;
    document.getElementById("query_temp_press").disabled = false;
    document.getElementById("query_magn").disabled = false;
    document.getElementById("query_acc").disabled = false;
    document.getElementById("query_gyro").disabled = false;
    document.getElementById("query_IMU").disabled = false;
  },

  onQueryTempButtonClick: function () {
    document.getElementById("temp_text").innerHTML = "Loading";
    $ajax({ url: "http://192.168.1.102:5000/temperature" })
      .done(function (data) {
        document.getElementById("query_temp").disabled =
          data.temp + " @ time: " + data.time_stamp;
      })
      .fail(function () {
        alert("Failure!");
      })
      .always(function () {
        alert("Always!");
      });
  },

  onQueryPressButtonClick: function () {
    document.getElementById("press_text").innerHTML = "Loading";
    $ajax({ url: "http://192.168.1.102:5000/pressure" })
      .done(function (data) {
        document.getElementById("query_press").disabled =
          data.pressure + " @ time: " + data.time_stamp;
      })
      .fail(function () {
        alert("Failure!");
      })
      .always(function () {
        alert("Always!");
      });
  },

  onQueryTempPressButtonClick: function () {
    document.getElementById("temp_press_text").innerHTML = "Loading";
    $ajax({ url: "http://192.168.1.102:5000/temperature/pressure" })
      .done(function (data) {
        document.getElementById("query_temp_press").disabled =
          data.temp_p + " @ time: " + data.time_stamp;
      })
      .fail(function () {
        alert("Failure!");
      })
      .always(function () {
        alert("Always!");
      });
  },

  onQueryHumButtonClick: function () {
    document.getElementById("hum_text").innerHTML = "Loading";
    $ajax({ url: "http://192.168.1.102:5000/humidity" })
      .done(function (data) {
        document.getElementById("query_press").disabled =
          data.humidity + " @ time: " + data.time_stamp;
      })
      .fail(function () {
        alert("Failure!");
      })
      .always(function () {
        alert("Always!");
      });
  },

  onQueryTempHumButtonClick: function () {
    document.getElementById("temp_hum_text").innerHTML = "Loading";
    $ajax({ url: "http://192.168.1.102:5000/temperature/pressure" })
      .done(function (data) {
        document.getElementById("query_temp_hum").disabled =
          data.temp_h + " @ time: " + data.time_stamp;
      })
      .fail(function () {
        alert("Failure!");
      })
      .always(function () {
        alert("Always!");
      });
  },

  onQueryMagnButtonClick: function () {
    document.getElementById("magn_text").innerHTML = "Loading";
    $ajax({ url: "http://192.168.1.102:5000/compass" })
      .done(function (data) {
        document.getElementById("query_magn").disabled =
          data.compass + " @ time: " + data.time_stamp;
      })
      .fail(function () {
        alert("Failure!");
      })
      .always(function () {
        alert("Always!");
      });
  },

  onQueryAccButtonClick: function () {
    document.getElementById("acc_text").innerHTML = "Loading";
    $ajax({ url: "http://192.168.1.102:5000/accelerometer" })
      .done(function (data) {
        document.getElementById("query_acc").disabled =
          data.pitch_acc +
          " @ time: " +
          data.time_stamp +
          data.roll_acc +
          " @ time: " +
          data.time_stamp +
          data.yaw_acc +
          " @ time: " +
          data.time_stamp;
      })
      .fail(function () {
        alert("Failure!");
      })
      .always(function () {
        alert("Always!");
      });
  },

  onQueryGyroButtonClick: function () {
    document.getElementById("gyro_text").innerHTML = "Loading";
    $ajax({ url: "http://192.168.1.102:5000/gyrosocope" })
      .done(function (data) {
        document.getElementById("query_press").disabled =
          data.pitch_gyro +
          " @ time: " +
          data.time_stamp +
          data.roll_gyro +
          " @ time: " +
          data.time_stamp +
          data.yaw_gyro +
          " @ time: " +
          data.time_stamp;
      })
      .fail(function () {
        alert("Failure!");
      })
      .always(function () {
        alert("Always!");
      });
  },

  onQueryIMUButtonClick: function () {
    document.getElementById("IMU_text").innerHTML = "Loading";
    $ajax({ url: "http://192.168.1.102:5000/pressure" })
      .done(function (data) {
        document.getElementById("query_press").disabled =
          data.pitch_IMU +
          " @ time: " +
          data.time_stamp +
          data.roll_IMU +
          " @ time: " +
          data.time_stamp +
          data.yaw_IMU +
          " @ time: " +
          data.time_stamp;
      })
      .fail(function () {
        alert("Failure!");
      })
      .always(function () {
        alert("Always!");
      });
  },
};

// Initialize app
app.initialize();
