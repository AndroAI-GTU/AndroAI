import React, { useState } from 'react';

function Question() {
	const [data, setData] = useState({
		appName: '',
		activityCount: '',
		activityNames: '',
		activityConnections: '',
		activityElements: '',
		elementFunctions: '',
		appIcon: null,
	});

	const handleChange = (e) => {
		const { name, value } = e.target;
		setData({
		...data,
		[name]: value,
		});
	};

	const handleFileChange = (e) => {
		console.log(e.target.files[0]);
		setData({
		...data,
		appIcon: e.target.files[0],
		});
	};

	const handleSubmit = async (e) => {
		e.preventDefault();
		const formData = new FormData();
		formData.append('appName', data.appName);
		formData.append('activityCount', data.activityCount);
		formData.append('activityNames', data.activityNames);
		formData.append('activityConnections', data.activityConnections);
		formData.append('activityElements', data.activityElements);
		formData.append('elementFunctions', data.elementFunctions);
		formData.append('appIcon', data.appIcon);
		
		try {
			const res = await fetch("http://localhost:5000/user/query", {
				method: "POST",
				body: formData,
			});

			if (!res.ok) {
				throw new Error(`HTTP error! status: ${res.status}`);
			}

			const openRes = await res.json();
			console.log(openRes);
		} catch (error) {
			console.error('Error fetching data:', error);
		}
		console.log(data);
	};

  return (
	<div style={{ maxWidth: '600px', margin: '0 auto', padding: '20px', fontFamily: 'Arial, sans-serif',backgroundColor:"gray" }}>
	  <h1 style={{ textAlign: 'center' }}>Application Form</h1>
	  <form onSubmit={handleSubmit}>
		<label htmlFor="appName">Application Name:</label>
		<input
		  type="text"
		  id="appName"
		  name="appName"
		  value={data.appName}
		  onChange={handleChange}
		  required
		  style={{ width: '100%', padding: '10px', marginTop: '5px' }}
		/>

		<label htmlFor="activityCount">Number of Activities :</label>
		<input
		  type="number"
		  id="activityCount"
		  name="activityCount"
		  value={data.activityCount}
		  onChange={handleChange}
		  required
		  style={{ width: '100%', padding: '10px', marginTop: '5px' }}
		/>

		<label htmlFor="activityNames">Name of the Activities :</label>
		<textarea
		  id="activityNames"
		  name="activityNames"
		  value={data.activityNames}
		  onChange={handleChange}
		  rows="5"
		  required
		  style={{ width: '100%', padding: '10px', marginTop: '5px' }}
		></textarea>

		<label htmlFor="activityConnections">Interconnection of activities:</label>
		<textarea
		  id="activityConnections"
		  name="activityConnections"
		  value={data.activityConnections}
		  onChange={handleChange}
		  rows="5"
		  required
		  style={{ width: '100%', padding: '10px', marginTop: '5px' }}
		></textarea>

		<label htmlFor="activityElements"> Items in activities:</label>
		<textarea
		  id="activityElements"
		  name="activityElements"
		  value={data.activityElements}
		  onChange={handleChange}
		  rows="5"
		  style={{ width: '100%', padding: '10px', marginTop: '5px' }}
		></textarea>

		<label htmlFor="elementFunctions">Text explaining the functions of the elements:</label>
		<textarea
		  id="elementFunctions"
		  name="elementFunctions"
		  value={data.elementFunctions}
		  onChange={handleChange}
		  rows="5"
		  style={{ width: '100%', padding: '10px', marginTop: '5px' }}
		></textarea>

		<label htmlFor="appIcon">App Icon (Launcher) - Upload as a photo:</label>
		<input
		  type="file"
		  id="appIcon"
		  name="appIcon"
		  accept="image/*"
		  onChange={handleFileChange}
		  required
		  style={{ marginTop: '5px' }}
		/>
		
		<button type="submit" style={{ display: 'block', width: '100%', padding: '10px', backgroundColor: '#4CAF50', color: 'white', border: 'none', textAlign: 'center', marginTop: '20px', cursor: 'pointer' }}>
		  Send
		</button>
	  </form>
	</div>
  );
}

export default Question;
