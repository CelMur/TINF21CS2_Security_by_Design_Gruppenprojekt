const API_URL = 'http://localhost:8000/api/v1';  // Replace with your API's URL


function registerUser(data) {
    $.ajax({
        url: `${API_URL}/register/`,
        type: 'POST',
        dataType: 'json',
        data: JSON.stringify(data),
        contentType: 'application/json',
        success: function(response) {
            console.log('User registered successfully');
        },
        error: function(error) {
            console.log('Error in registration: ', error);
        }
    });
}

function login(data) {
    $.ajax({
        url: `${API_URL}/auth/`,
        type: 'POST',
        dataType: 'json',
        data: JSON.stringify(data),
        contentType: 'application/json',
        success: function(response) {
            console.log('User logged in successfully');
        },
        error: function(error) {
            console.log('Error in login: ', error);
        }
    });
}


function createAddress(data) {
    return $.ajax({
        url: `${API_URL}/adress/`,
        method: 'POST',
        dataType: 'json',
        data: JSON.stringify(data),
        contentType: 'application/json',
    });
}



function createContract(data) {
    $.ajax({
        url: `${API_URL}/contract/`,
        type: 'POST',
        dataType: 'json',
        data: JSON.stringify(data),
        contentType: 'application/json',
        success: function(response) {
            console.log('Contract created successfully');
        },
        error: function(error) {
            console.log('Error in contract creation: ', error);
        }
    });
}


function updateProfile(data) {
    $.ajax({
        url: `${API_URL}/update-profile/`,
        type: 'PUT',
        dataType: 'json',
        data: JSON.stringify(data),
        contentType: 'application/json',
        success: function(response) {
            console.log('Profile updated successfully');
        },
        error: function(error) {
            console.log('Error in profile update: ', error);
        }
    });
}

function deleteProfile() {
    $.ajax({
        url: `${API_URL}/delete-profile/`,
        type: 'DELETE',
        dataType: 'json',
        contentType: 'application/json',
        success: function(response) {
            console.log('Profile deleted successfully');
        },
        error: function(error) {
            console.log('Error in profile deletion: ', error);
        }
    });
}


export { 
    registerUser, login, 
    createAddress, 
    createContract,
    updateProfile, deleteProfile
};