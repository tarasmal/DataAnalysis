def linear_regression(x, y):
    import numpy as np
    from sklearn.linear_model import LinearRegression
    x = np.array(x).reshape(-1, 1)
    print(x)
    y = np.array(y)
    model = LinearRegression() # Create an instance of the class LinearRegression, which will represent the regression model
    model.fit(x, y)

    return model.predict(x)