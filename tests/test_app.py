'''actual tests here'''

import pytest

#homepage
def test_homepage_good(client):
    '''tests that the homepage can be reached properly'''
    res = client.get("/")
    assert res.status_code == 200


# valid request
def test_good_image(client):
    '''tests apropriate response from proper image'''
    with open("test_images/2/Sign 2 (87).jpeg","rb") as img:
        res = client.post("/prediction",
            data={"file":(img,"Sign 2 (87).jpeg")},
            content_type="multipart/form-data"
        )
    assert res.status_code==200
    assert b"2" in res.data

#invalid request
def test_invalid_method(client):
    '''tests that unallowed methods aren't allowed'''
    res = client.get("/prediction")
    assert res.status_code == 405

#missing file request
def test_missing_file(client):
    '''tests file missing'''
    res=client.post("/prediction",
        data={},
        content_type="multipart/form-data"
    )
    assert res.status_code==200 
    #app never sends fail, it just tells users that it didn't work, but the page loads and all that
    assert b"File cannot be processed." in res.data

def test_not_image(client):
    '''tests file that isn't image'''
    with open("test_images/notimage/text.txt","rb") as notimg:
        res = client.post("/prediction",
            data={"file":(notimg,"text.txt")},
            content_type="multipart/form-data"
        )
    assert res.status_code==200
    assert b"File cannot be processed." in res.data

#missing not done

#bad input handled

# preproccers or prediction
