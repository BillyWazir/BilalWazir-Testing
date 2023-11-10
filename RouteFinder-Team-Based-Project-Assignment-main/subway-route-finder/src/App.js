import React, { useState, useEffect } from 'react';
import './App.css';
import logo from './RFlogo.png'; // Adjust the path accordingly

function Legend({ lines }) {
  console.log(lines);
  return (
    <div className="legend">
      <h3>Legend</h3>
      {Object.entries(lines).map(([lineName, color]) => (
        <div key={lineName} className="legend-item">
          <span className="line-color" style={{ backgroundColor: color }}></span>
          <span className="line-name">{lineName}</span>
        </div>
      ))}
    </div>
  );
}

function App() {
  const [stations, setStations] = useState([]);
  const [startStation, setStartStation] = useState('');
  const [endStation, setEndStation] = useState('');
  const [route, setRoute] = useState([]);
  const [statusMessage, setStatusMessage] = useState('');
  const [favorites, setFavorites] = useState([]);
  const lineColors = {
    // Define your line colors here
    "Booch Line": "#FFD700",
    "Wirfs-Brock Line": "#FF0000",
    "Rumbaugh Line": "#00FF00",
    "Jacobson Line": "#0000FF",
    "Liskov Line": "#FF00FF",
    "Meyer Line": "#FF69B4",
    "Gamma Line": "#FF4500"
  };

  const getLineColor = (lineName) => {
    return lineColors[lineName] || "#000"; // Default color if line not found
  };

  const fetchRoute = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/route?start=${startStation}&end=${endStation}`);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      if (data.length === 0) {
        // No route found
        setStatusMessage("No route exists between the selected stations.");
        setRoute([]);
      } else {
        // Route found
        setRoute(data);
        setStatusMessage("Route found successfully!");
      }
    } catch (error) {
      console.error('Failed to fetch route:', error);
      setStatusMessage("Failed to fetch route.");
    }
  };

  const handleFavorite = (start, end) => {
    const newFavorite = { start, end };
    setFavorites(prevFavorites => {
      // Check if the route is already in favorites
      if (prevFavorites.some(fav => fav.start === start && fav.end === end)) {
        // Remove from favorites
        return prevFavorites.filter(fav => !(fav.start === start && fav.end === end));
      } else {
        // Add to favorites
        return [...prevFavorites, newFavorite];
      }
    });
  };

  useEffect(() => {
    fetch('http://127.0.0.1:5000/stations')
      .then(response => response.json())
      .then(data => setStations(data))
      .catch(error => console.error('Failed to fetch stations:', error));
  }, []);

  return (
    <div className="App">
      <img src={logo} alt="Your Logo" className="logo" />
      <h1>Subway Routefinder</h1>

      {/* Favorites Section */}
      <div className="favorites">
        <h3>Favorites</h3>
        {favorites.map((fav, index) => (
          <div key={index} className="favorite-item" onClick={() => {
            setStartStation(fav.start);
            setEndStation(fav.end);
            fetchRoute();
          }}>
            {fav.start} to {fav.end}
          </div>
        ))}
      </div>

      {/* Rest of the UI */}
      <label>
        Start Station:
        <select 
          value={startStation} 
          onChange={e => setStartStation(e.target.value)}
        >
          <option value="">Select a station</option>
          {stations.map(station => (
            <option key={station} value={station}>
              {station}
            </option>
          ))}
        </select>
      </label>

      <label>
        End Station:
        <select 
          value={endStation} 
          onChange={e => setEndStation(e.target.value)}
        >
          <option value="">Select a station</option>
          {stations.map(station => (
            <option key={station} value={station}>
              {station}
            </option>
          ))}
        </select>
      </label>

      <button onClick={fetchRoute}>
        Find Route
      </button>

      {statusMessage && <p>{statusMessage}</p>} {/* Display status message */}

      {/* Display the fetched route */}
      {route.length > 0 && (
        <div>
          <div className="route-details">
            <h2>Route Details:</h2>
            <div className="route-visual">
              {/* Render the starting station */}
              <div className="station">
                <div className="station-icon start">Start Here</div>
                <div className="station-name">{route[0].start}</div>
              </div>

              {/* Render the intermediate stations */}
              {route.slice(1, -1).map((segment, index) => (
                <div key={index} className="station intermediate">
                  <div className="station-name">{segment.end}</div>
                  <div className="line" style={{ backgroundColor: getLineColor(segment.line) }}></div>
                </div>
              ))}

              {/* Render the ending station */}
              <div className="station">
                <div className="station-icon end">End Here</div>
                <div className="station-name">{route[route.length - 1].end}</div>
              </div>
            </div>
          </div>

          <button onClick={() => handleFavorite(route[0].start, route[route.length - 1].end)}>
            Add to Favorites
          </button>
        </div>
      )}

      {/* Render the legend component */}
      <Legend lines={lineColors} />
    </div>
  );
}

export default App;

