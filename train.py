from flash.tabular import TabularRegressionData, TabularRegressor

# 1. Create the DataModule

# 'type',
# 'required_age',
# 'is_free',
# 'platform_windows',
# 'platform_mac',
# 'platform_linux',
# 'metacritic_score',
# 'categories_array', -- ignore
# 'genres_array', -- ignore
# 'recommendations',
# 'first_group_price_cents',
# 'days_since_release'

cols_string=["type", "platform_windows", "platform_mac", "platform_linux", "is_free"]
cols_numerical=["required_age", "metacritic_score", "recommendations", "days_since_release"]

datamodule = TabularRegressionData.from_csv(
    categorical_fields=cols_string,
    numerical_fields=cols_numerical,
    target_fields="first_group_price_cents",
    train_file="./ml_games.csv",
    val_split=0.2,
    batch_size=64,
)