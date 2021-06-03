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
  // Variable
  counter: 0,

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
    document.getElementById("increment_button").addEventListener(
      "click", // Device must be ready (Cordova environment)
      app.onAddButtonClick.bind(app), // Run application
      false
    );
    document.getElementById("reset_button").addEventListener(
      "click", // Device must be ready (Cordova environment)
      app.onResetButtonClick.bind(app), // Run application
      false
    );
    document.getElementById("increment_button").disabled = false;
    document.getElementById("reset_button").disabled = false;
  },

  onAddButtonClick: function () {
    app.counter += 1;
    document.getElementById("value_text").innerHTML =
      "Counter Value: " + app.counter;
  },

  onResetButtonClick: function () {
    app.counter = 0;
    document.getElementById("value_text").innerHTML =
      "Counter Value: " + app.counter;
  },
};

// Initialize app
app.initialize();
